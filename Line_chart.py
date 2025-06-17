import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('numer.csv')


countries = ['United States', 'Germany', 'Japan', 'Mexico', 'Iran', 'China', 'India', 'Ethiopia']
selected = df[df['Entity'].isin(countries)].copy()


age_columns = [
    'Prevalence - Neoplasms - Sex: Both - Age: Under 5 (Number)',
    'Prevalence - Neoplasms - Sex: Both - Age: 5-14 years (Number)',
    'Prevalence - Neoplasms - Sex: Both - Age: 15-49 years (Number)',
    'Prevalence - Neoplasms - Sex: Both - Age: 50-69 years (Number)',
    'Prevalence - Neoplasms - Sex: Both - Age: 70+ years (Number)'
]
age_labels = ['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years']


selected.loc[:, 'Total'] = selected[age_columns].sum(axis=1)


for i, col in enumerate(age_columns):
    selected.loc[:, f'Ratio_{age_labels[i]}'] = selected[col] / selected['Total']


plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
colors = plt.cm.tab10.colors[:len(countries)]


plt.figure(figsize=(14, 8))


for i, country in enumerate(countries):
    country_data = selected[selected['Entity'] == country]
    ratios = [country_data[f'Ratio_{age}'].values[0] for age in age_labels]

    plt.plot(age_labels, ratios,
             marker='o',
             markersize=8,
             linewidth=2.5,
             color=colors[i],
             label=country)

plt.title('Cancer Prevalence by Age Group in Different Countries (2015)', fontsize=16)
plt.ylabel('Proportion of Cases', fontsize=12)
plt.xlabel('Age Group', fontsize=12)
plt.ylim(0, 0.7)
plt.yticks(np.arange(0, 0.71, 0.1), fontsize=10)
plt.legend(title='Country', fontsize=10, title_fontsize=11,
           loc='upper center', bbox_to_anchor=(0.5, -0.15),
           ncol=4, fancybox=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.subplots_adjust(bottom=0.2)
plt.savefig('cancer_age_distribution_by_country.png', dpi=300, bbox_inches='tight')
plt.show()


plt.figure(figsize=(14, 8))


bottom = np.zeros(len(countries))
ratios_data = [selected[f'Ratio_{age}'].values for age in age_labels]


for i, age in enumerate(age_labels):
    plt.bar(countries, ratios_data[i],
            bottom=bottom,
            color=colors[i % len(colors)],
            edgecolor='white',
            label=f'{age}')
    bottom += ratios_data[i]

plt.title('Stacked Distribution of Cancer Cases by Age Group (2015)', fontsize=16)
plt.ylabel('Proportion of Cases', fontsize=12)
plt.xlabel('Country', fontsize=12)
plt.ylim(0, 1.05)
plt.xticks(fontsize=10, rotation=15)
plt.yticks(np.arange(0, 1.1, 0.2), fontsize=10)


plt.legend(title='Age Group', fontsize=10, title_fontsize=11,
           loc='upper left', bbox_to_anchor=(1.02, 1),
           borderaxespad=0.)

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.subplots_adjust(right=0.8)
plt.savefig('cancer_age_distribution_stacked.png', dpi=300, bbox_inches='tight')
plt.show()



