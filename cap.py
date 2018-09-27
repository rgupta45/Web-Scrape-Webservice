import requests
import re
from bs4 import BeautifulSoup
url ='https://alerts.weather.gov/cap/us.php?x=0'
resp = requests.get(url)
soup = BeautifulSoup(resp.content,features='xml')
#print(soup.prettify())
geocode = soup.find_all('cap:geocode')
#print(geocode[0])
codes={}
count=0
for geo in enumerate(geocode):
    geo_split = re.split('<',str(geo[1]))
    #print(len(geo_split))
    for i in enumerate(geo_split):
        if geo_split[i[0]][-5:]=='FIPS6':
            if geo_split[i[0]+2][6:] not in codes:
                codes[geo_split[i[0]+2][6:]]=['FIPS6',geo[0]]
        elif geo_split[i[0]][-3:]=='UGC':
            if geo_split[i[0]+2][6:] not in codes:
                codes[geo_split[i[0] + 2][6:]] = ['UGC', geo[0]]
    count=count+1
print(codes)# this is a dictionary item
print(count)# check how many times rep happened