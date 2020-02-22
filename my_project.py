import pandas as pd
import numpy as np

data = pd.read_csv('books.csv',error_bad_lines=False)
data.rename(columns={'# num_pages': 'pages_number'},inplace=True)
print(data.columns)
print(data.dtypes)
print(data.shape)
print(data.describe())
print(data.info())
print(data.isnull().sum())
with pd.option_context('display.max_columns',8):
    print(data.corr())
