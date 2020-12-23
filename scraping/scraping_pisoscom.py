import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import numpy as np


##########       GET ALL THE LINKS ONE PAGE        ############

base_url = 'https://www.pisos.com/venta/pisos-valencia_capital/hasta-120000/'

# request and create bs
pisos = requests.get(base_url)
soup = BeautifulSoup(pisos.content, 'html.parser')

num_iter = len(soup.select('div[itemtype="http://schema.org/SingleFamilyResidence"]'))

urls_page = []
urls_page.append(base_url)
#create link pages
for i in range(2, 76):
    urls_page.append(base_url+ str(i) +'/')



# ### Create urls list for each add per page
def getting_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    num_iter = len(soup.select('div[itemtype="http://schema.org/SingleFamilyResidence"]'))

    urls = []
    for i in range(num_iter):
        ref = soup.select('div[itemtype="http://schema.org/SingleFamilyResidence"]')[i].get('data-navigate-ref')
        base = 'https://www.pisos.com'
        url = base+ref
        urls.append(url)

    return urls


house_urls = []
for url in urls_page:
    print(url)
    house_urls.append(getting_url(url))
    wait_time = np.random.randint(1, 4)
    sleep(wait_time)


# print(getting_url(urls_page[0]))

print(house_urls)


