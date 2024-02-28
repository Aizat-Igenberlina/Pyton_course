unique_values = data['WhoAmI'].unique()
one_hot_data=pd.DataFrame()

for value in unique_values:
    one_hot_data[value]=(data['WhoAmI'] == value).astype(int)

one_hot_data.head()
