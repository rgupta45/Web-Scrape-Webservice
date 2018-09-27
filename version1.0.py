import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd

#Extraction from web start----
def extract_web():
    url = 'https://alerts.weather.gov/cap/us.php?x=0'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features='xml')
    events = soup.find_all('cap:event')
    geocode = soup.find_all('cap:geocode')

    event_list = []
    for index, event in enumerate(events):
        event_split = re.split('<', str(event))
        event_list.append(event_split[1][10:])

    codes = {}
    count = 0
    for geo in enumerate(geocode):
        geo_split = re.split('<', str(geo[1]))
        # print(len(geo_split))
        for i in enumerate(geo_split):
            if geo_split[i[0]][-5:] == 'FIPS6':
                if geo_split[i[0] + 2][6:] not in codes:
                    codes[geo_split[i[0] + 2][6:]] = ['FIPS6', geo[0]]
            elif geo_split[i[0]][-3:] == 'UGC':
                if geo_split[i[0] + 2][6:] not in codes:
                    codes[geo_split[i[0] + 2][6:]] = ['UGC', geo[0]]
        count = count + 1

    for keys, values in (sorted(codes.items(), key=lambda x: x[1][1])):
        i = values[1]
        values.append(event_list[i])
    #print(event_list)
    #print(len(event_list))
    #print(count)
    #print(codes)

    # Extraction from web finish----
    # data frame conversion Start--
    final_array = []
    for key, value in sorted(codes.items(), key=lambda x: x[1][1]):
        if (value[1] < count) and (value[0] == 'FIPS6'):
            key_split = re.split(' ', key)
            for ind, ke_sp in enumerate(key_split):
                final_array.append([ke_sp, value[0], value[2]])

    df = pd.DataFrame(np.array(final_array), columns=['CodeNumber', 'TypeCode', 'Event'])
    #print(df)
    # data frame conversion End--
    return df
print(extract_web())



