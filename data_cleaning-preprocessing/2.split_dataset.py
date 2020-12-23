import pandas as pd 

data = pd.read_csv('./Scrape Idealista/master_data.csv')

data.rename(columns={'neighbourhood':'district', 'district':'neighbourhood'}, inplace=True)

print(data)


### Divide DataFrame into two Dataframes depending on wether they have address and district

data_same = pd.DataFrame(columns=['index', 'address', 'district', 'neighbourhood', 'sqft_surface',
       'bedrooms', 'bathrooms', 'new_construction', 'price'])
data_dif = pd.DataFrame(columns=['index', 'address', 'district', 'neighbourhood', 'sqft_surface',
       'bedrooms', 'bathrooms', 'new_construction', 'price'])
x = 0
for a, b in zip(data['address'], data['district']):

    if a in b or a == 'Valencia' or a=='V':
        as_data = data.iloc[x]
        data_same = pd.concat([as_data, data_same], axis=1)
             
    else:
        us_data = data.iloc[x]
        data_dif = pd.concat([us_data, data_dif], axis=1)

    x += 1

data_same = data_same.transpose().iloc[:-9]
data_dif = data_dif.transpose().iloc[:-9]


dt = data_dif
ds = data_same

### Divide DataFrame into two Dataframes depending on wether they have address and neighbourhood

data_same2 = pd.DataFrame(columns=['index', 'address', 'district', 'neighbourhood', 'sqft_surface',
   'bedrooms', 'bathrooms', 'new_construction', 'price'])
data_dif2 = pd.DataFrame(columns=['index', 'address', 'district', 'neighbourhood', 'sqft_surface',
   'bedrooms', 'bathrooms', 'new_construction', 'price'])
x = 0

for a, b in zip(dt['address'], dt['neighbourhood']):
    if a in b:
        as_data = dt.iloc[x]
        print(type(as_data))
        
        data_same2 = pd.concat([as_data, data_same2], axis=1)
    
    else:
        print(us_data)
        us_data = pd.DataFrame(dt.iloc[x])
        data_dif2 = pd.concat([us_data, data_dif2], axis=1)
    x += 1

data_same2 = data_same2.transpose().iloc[:-9]
data_dif2 = data_dif2.transpose().iloc[:-9]

dif_data = data_dif2

same_data = pd.concat([data_same, data_same2], axis=0)


dif_data.to_csv('Dif_data.csv', index=False)
same_data.to_csv('Same_data.csv', index=False)
