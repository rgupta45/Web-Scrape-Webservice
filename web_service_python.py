import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize
from flask import Flask, request, jsonify

app = Flask(__name__) #create the Flask app
@app.route('/fips6')
def default():
    code = request.args['code']
    with open('final_county.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    df = json_normalize(data['features'])#df.shape[0]
    df['count_poly'] = [len(i) for i in df['geometry.coordinates']]
    df['fips6']=[str(0)+str(i[0]+str(i[1])) for i in zip(df['properties.STATE'],df['properties.COUNTY'])]
    df['fips5']=[str(i[0]+str(i[1])) for i in zip(df['properties.STATE'],df['properties.COUNTY'])]
    if len(code)==6:
        ret_df= df[df['fips6']==code]
        ret_df.reset_index(drop=True,inplace=True)
        ret_json= ret_df.to_json()
        return jsonify(ret_json), 200
    else:
        ret_df= df[df['fips5']==code]
        ret_df.reset_index(drop=True,inplace=True)
        ret_json= ret_df.to_json()
        return jsonify(ret_json), 200

if __name__ == '__main__':
    app.run(debug=True)