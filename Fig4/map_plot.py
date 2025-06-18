import pandas as pd
import plotly.express as px
import os
import csv


FILE_PATH = "07 share-of-population-with-cancer-by-age.csv"
HTML_PATH = "cancer_prevalence_map_1990-2015.html"
CSV_PATH = "processed_cancer_data_1990-2015.csv"


def process_cancer_data(file_path):

    try:

        with open(file_path, 'r') as f:
            sample = f.read(5000)
            dialect = csv.Sniffer().sniff(sample)
            separator = dialect.delimiter


        df = pd.read_csv(
            file_path,
            sep=separator,
            engine='python',
            skipinitialspace=True
        )


        df.columns = [
            'Entity', 'Code', 'Year', 'Under5', '70+',
            '15-49', '50-69', '5-14', 'AllAges'
        ]


        df = df[(df['Year'] >= 1990) & (df['Year'] <= 2015)]
        #print(f"筛选后数据维度：{df.shape[0]}行×{df.shape[1]}列")
        print(f"年份范围：{df['Year'].min()} - {df['Year'].max()}")

        return df

    except Exception as e:
        print(f"数据处理失败：{str(e)}")
        with open(file_path, 'r') as f:
            lines = [next(f).strip() for _ in range(3)]
            print("文件前3行示例：")
            for i, line in enumerate(lines):
                print(f"行 {i + 1}: {line}")
        return pd.DataFrame()


if __name__ == "__main__":

    df = process_cancer_data(FILE_PATH)

    if not df.empty:

        fig = px.choropleth(
            df,
            locations="Code",
            color="70+",
            animation_frame="Year",
            hover_name="Entity",
            hover_data={
                '70+': ':.2f%',
                '50-69': ':.2f%',
                'AllAges': ':.2f%',
                'Year': True,
                'Code': False
            },
            color_continuous_scale="OrRd",
            range_color=(0, df['70+'].max()),
            labels={'70+': '70+岁患病率 (%)'},
            title="全球70岁以上人群癌症患病率变化 (1990-2015)",
            projection='natural earth'
        )


        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 800
        fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 600


        fig.update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=True,
                landcolor='rgb(240, 240, 240)',
                lakecolor='rgb(255, 255, 255)'
            ),
            margin={"r": 20, "t": 80, "l": 20, "b": 20},
            coloraxis_colorbar={
                'title': '患病率 %',
                'thickness': 15,
                'len': 0.7,
            }
        )


        fig.update_geos(
            showcountries=True,
            countrycolor="gray",
            countrywidth=0.3
        )


        fig.write_html(HTML_PATH)
        df.to_csv(CSV_PATH, index=False)



