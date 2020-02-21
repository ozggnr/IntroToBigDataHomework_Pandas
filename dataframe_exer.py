import pandas as pd
ins_data = pd.read_csv('insurance.csv')
print(ins_data)
print(ins_data.dtypes)
print(type(ins_data))
print(ins_data.index)
print(ins_data.shape)
print(ins_data.info())
print(ins_data.to_string())
print(ins_data.describe())
print(ins_data.columns)
print(ins_data['age'])
print(ins_data[['age','children','charges']])
print(ins_data[['age','children','charges']].head())
print(ins_data['charges'].min())
print(ins_data['charges'].max())
print(ins_data['charges'].mean())   #print(ins_data['charges'].describe()) for all statistics
print(ins_data[['age','sex','smoker','charges']][ins_data['charges'] == 10797.3362])
print(ins_data[['age','charges']][ins_data['charges'] == ins_data['charges'].max() ])
print(ins_data['region'].value_counts())
print(sum(ins_data['children']))
print(ins_data['charges'].corr(ins_data['age']))  #there is positive correlation between charges and age as i expected
print(ins_data['bmi'].corr(ins_data['children'])) # there is weak correlation between bmi and children
