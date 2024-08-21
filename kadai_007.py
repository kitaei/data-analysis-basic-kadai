import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

df = pd.read_csv('sample_pandas_6.csv')

category_df = pd.read_csv('category.csv')
category_df

df = pd.merge(df, category_df[['商品番号', 'カテゴリー']], how='inner', on='商品番号')
df

df['カテゴリー'].value_counts()
df['カテゴリー'].value_counts().plot(kind='bar')
plt.show()