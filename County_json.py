import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pprint import pprint
with open('final_county.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

df = json_normalize(data['features'])#df.shape[0]
df['count'] = [len(i) for i in df['geometry.coordinates']]


final_array = []
for i in range(1):
    county = df.iloc[i]['properties.COUNTY']
    state  = df.iloc[i]['properties.STATE']
    fips6 = str(0)+str(state)+str(county)
    County_name = df.iloc[i]['properties.NAME']
    final_array.append([fips6,County_name])
    for index,value in enumerate(df.iloc[i]['geometry.coordinates']):
        print(index,value)


#print('saadjajdnakjsdnkjaskdnansdkankdkjasnd')
#print(min(df.iloc[0]['geometry.coordinates'],key=len))

#print(np.array(final_array))
#pprint(dataframe)
#print(len(df.iloc[0]['geometry.coordinates']))

#pprint(df.iloc[0]['properties.COUNTY'])
#pprint(df.iloc[0]['properties.GEO_ID'])
#pprint(df.iloc[0]['properties.STATE'])
#pprint(final_array)
#pprint(df.iloc[1]['properties.COUNTY'])
#pprint(df.iloc[1]['properties.GEO_ID'])
#pprint(df.iloc[1]['properties.STATE'])
print(df.iloc[0])



