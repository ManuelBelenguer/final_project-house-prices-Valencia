import pandas as pd 
from geopy.geocoders import Nominatim
import time
from pprint import pprint

# dif_data = pd.read_csv('./Dif_data.csv')
data_same = pd.read_csv('./Same_data.csv')


# Correct one row
indexNames = dif_data[dif_data['address'] == 'Camins Al Grau - Penya - Roja - Avda. Francia'].index
# Delete these row indexes from dataFrame
dif_data.drop(indexNames , inplace=True)


app = Nominatim(user_agent="tutorial")

### Look for coordinates in data_dif
latitude_dif = []
longitude_dif = []
to_check = pd.DataFrame(columns=['index', 'address', 'district', 'neighbourhood', 'sqft_surface',
       'bedrooms', 'bathrooms', 'new_construction', 'price'])
x = 0
for i in range(len(dif_data)):
    print(i)
    print(dif_data['address'].iloc[i])
    try:
        hola = dif_data['address'].iloc[i], dif_data['district'].iloc[i], "Valencia, España"
        location = app.geocode(hola).raw
        latitude_dif.append(location['lat'])
        longitude_dif.append(location['lon'])
        time.sleep(1)
        x += 1
        print(hola)
        print('OK!')
    except:
        pass
        longitude_dif.append('None')
        latitude_dif.append('None')
        pd.concat([dif_data.iloc[i], to_check], axis=1)
        print(hola)
        print('NOPE!')

# Create columns with location info and append to data_dif
dif_data_location = dif_data 
dif_data_location['latitude'] = latitude_dif
dif_data_location['longitude'] = longitude_dif



# I'm going to get many None values, therefore if location are None append to data same

for_samedata = dif_data_location[dif_data_location['longitude']=='None']
new_dif_data = dif_data_location[dif_data_location['longitude']!= 'None']

dif_data.to_csv('secure_dif.csv', index=False)
new_dif_data.to_csv('real_dif_data.csv', index=False)
for_samedata.to_csv('for_samedata.csv', index=False)


for_samedata2 = pd.read_csv("for_samedata.csv")
for_samedata2 = for_samedata2.drop(columns=['latitude', 'longitude'])



same_data_maybe = pd.concat([data_same, for_samedata2], axis=0)
same_data_maybe.to_csv('same_data_maybe.csv', index=False)