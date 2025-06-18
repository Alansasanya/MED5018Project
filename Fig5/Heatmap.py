import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy import stats


data2 = pd.read_csv('death_rate.csv', encoding='gbk')


avegdp = pd.read_csv('avegdp.csv')


merged = pd.merge(
    data2[['Code',
           'Deaths - Neoplasms - Sex: Both - Age: Under 5 (Rate)',
           'Deaths - Neoplasms - Sex: Both - Age: 70+ years (Rate)',
           'Deaths - Neoplasms - Sex: Both - Age: 5-14 years (Rate)',
           'Deaths - Neoplasms - Sex: Both - Age: 50-69 years (Rate)',
           'Deaths - Neoplasms - Sex: Both - Age: 15-49 years (Rate)']],
    avegdp[['Code', '2015']].rename(columns={'2015': 'GDP_per_capita'}),
    on='Code',
    how='inner'
)



def classify_income(gdp):
    if gdp >= 12535: return 'High'
    elif 4046 <= gdp < 12535: return 'Upper-middle'
    elif 1036 <= gdp < 4046: return 'Lower-middle'
    else: return 'Low'

merged['Income_Group'] = merged['GDP_per_capita'].apply(classify_income)


age_columns = [
    'Deaths - Neoplasms - Sex: Both - Age: Under 5 (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 5-14 years (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 15-49 years (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 50-69 years (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 70+ years (Rate)'
]
short_labels = ["Under5", "5-14y", "15-49y", "50-69y", "70+y"]  # 简化标签


income_groups = ['High', 'Upper-middle', 'Lower-middle']


corr_matrix_block = pd.DataFrame(index=income_groups, columns=short_labels)


for group in income_groups:
    subset = merged[merged['Income_Group'] == group]

    corr_vals = []
    for col in age_columns:
        corr, pval = stats.spearmanr(subset['GDP_per_capita'], subset[col])
        corr_vals.append(corr)
    corr_matrix_block.loc[group] = corr_vals


plt.figure(figsize=(10, 6))


cmap = LinearSegmentedColormap.from_list('custom_cmap', ['#2166ac', '#f7f7f7', '#b2182b'], N=256)


ax = sns.heatmap(
    corr_matrix_block.T.astype(float),
    annot=True,
    cmap=cmap,
    center=0,
    vmin=-1,
    vmax=1,
    fmt=".2f",
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={'label': 'Correlation Coefficient', 'shrink': 0.8},
    annot_kws={'size': 11, 'weight': 'bold'}
)


for i in range(1, len(income_groups)):
    ax.axvline(x=i, color='black', lw=2, alpha=0.7)
for i in range(1, len(short_labels)):
    ax.axhline(y=i, color='black', lw=1, alpha=0.5)


ax.set_title('GDP per Capita vs Cancer Mortality by Income Group (2015)',
             fontsize=15, pad=15, weight='bold')
ax.set_xlabel('Income Group', fontsize=12, labelpad=10)
ax.set_ylabel('Age Group', fontsize=12, labelpad=10)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(rotation=0, fontsize=10)


plt.tight_layout()
plt.savefig('gdp_income_block_heatmap_no_low.png', dpi=300, bbox_inches='tight')
plt.show()