Data cleaning

When firstly approaching this dataset, we find some missing values in certain columns and some values that weren't in the correct place. As they weren't many and I was running out of time I decided to drop them instead of improving the dataset. After droping the mentioned values we ended with a dataset of 7030 properties from a dataset of 7272. 

Data preprocessing

Based on the experience in previous projects, I thought that getting the exact location for the properties in the dataset will be good for the model to predict the house prices. Getting this data from web scraping was quite difficult so instead I decided to use a library called geopy.py that allows you to get the exact location (coordinates) of a place based on the addres, postal code, etc. 

This process took some time as requests need to be done to the geopy page, on the other hand some of the houses weren't providing the address and for some other the address (street name) was not recognized by geopy. That forced me to follow to differet approaches.
    - 1. Get the exact location of the properties that were providing a street name. Managed to get in total around 2400 with the exact location. 
    - 2. Get the location of the neighbourhood the properties are in. Some hesitation pops up when thinking of following this process as the information these coordinates are going to provide is going 
    be very similar to the information provided by neighbourhood variable. 
            
            note: as well see in the future this was not a good approach.
      

            
