import pandas as pd

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv"
df = pd.read_csv(url)

df_melt = df.melt(id_vars=['country', 'food_category'], var_name='metrics', value_name='measurements')
df_melt.to_csv("data/food_consumption2.csv", index=False)