import pandas as pd
import matplotlib.pyplot as plt

import matplotlib


matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Lucida Grande', 'Verdana']


file_path = '02 total-cancer-deaths-by-type.csv'
df = pd.read_csv(file_path)


df_filtered = df[(df['Year'] >= 1990) & (df['Year'] <= 2015)].copy()
print(f"Filtered data (1990-2015): {len(df_filtered)} rows")


df_countries = df_filtered[df_filtered['Code'].notna() &
                           df_filtered['Code'].str.contains('^[A-Z]{3}$')].copy()
print(f"Country data: {len(df_countries)} rows")


cancer_columns = [col for col in df.columns if 'Deaths -' in col and 'Number)' in col]
print(f"Identified cancer columns: {len(cancer_columns)}")


cancer_totals = df_countries[cancer_columns].sum()


top_6_cancers = cancer_totals.sort_values(ascending=False).head(6)
print("Top cancer types with death counts:")
print(top_6_cancers)



def get_cancer_name(full_name):

    parts = full_name.split(' - ')
    if len(parts) < 2:
        return full_name


    name_part = parts[1]


    name_mapping = {
        'Tracheal, bronchus, and lung': 'Lung',
        'Stomach': 'Stomach',
        'Liver': 'Liver',
        'Colon and rectum': 'Colorectal',
        'Breast': 'Breast',
        'Prostate': 'Prostate',
        'Pancreatic': 'Pancreatic',
        'Leukemia': 'Leukemia',
        'Non-Hodgkin lymphoma': 'Lymphoma (NHL)',
        'Bladder': 'Bladder',
        'Brain and central nervous system': 'Brain/CNS',
        'Cervical': 'Cervical',
        'Other neoplasms': 'Other Tumors',
        'Lip and oral cavity': 'Oral Cavity',
        'Kidney': 'Kidney',
        'Larynx': 'Larynx',
        'Gallbladder and biliary tract': 'Gallbladder',
        'Malignant skin melanoma': 'Melanoma',
        'Thyroid': 'Thyroid',
        'Uterine': 'Uterine',
        'Mesothelioma': 'Mesothelioma',
        'Nasopharynx': 'Nasopharynx',
        'Other pharynx': 'Pharynx (Other)',
        'Non-melanoma skin': 'Non-Melanoma Skin',
        'Hodgkin lymphoma': 'Lymphoma (Hodgkin)',
        'Multiple myeloma': 'Myeloma',
        'Testicular': 'Testicular'
    }

    for key, value in name_mapping.items():
        if key in name_part:
            return value


    return name_part.split()[0]


short_names = [get_cancer_name(name) for name in top_6_cancers.index]


plt.figure(figsize=(14, 8))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bars = plt.barh(short_names, top_6_cancers.values, color=colors, height=0.6)


for bar in bars:
    width = bar.get_width()
    plt.text(width * 1.005, bar.get_y() + bar.get_height() / 2,
             f'{int(width):,}',
             va='center', ha='left', fontsize=12)


plt.title('Top 6 Deadliest Cancer Types Worldwide (1990-2015)', fontsize=18, pad=20, weight='bold')
plt.xlabel('Total Deaths', fontsize=14, labelpad=10)
plt.ylabel('Cancer Type', fontsize=14, labelpad=15)


plt.xlim(0, top_6_cancers.max() * 1.25)
plt.grid(axis='x', linestyle='--', alpha=0.4)
plt.gca().invert_yaxis()




total_deaths = int(top_6_cancers.sum())
total_percentage = int((top_6_cancers.sum() / cancer_totals.sum()) * 100)
plt.figtext(0.05, 0.95, f"Top 6 account for {total_percentage}% of all cancer deaths",
            fontsize=12, bbox=dict(facecolor='white', alpha=0.8))


plt.xticks(fontsize=12)
plt.yticks(fontsize=13)
plt.tight_layout(rect=[0, 0.03, 1, 0.97])


plt.savefig('top_6_deadliestcancers.png', dpi=300, bbox_inches='tight')
plt.show()

