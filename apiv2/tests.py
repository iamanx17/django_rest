import requests
import json


def post_data():
    url='http://127.0.0.1:8000/api/'
    data={
        'name':'admin',
        'roll':314090,
        'city':'Delhi',
    }

    json_data=json.dumps(data)

    r=requests.post(url=url, data=json_data)

    print(r.json())

def get_data():
    url='http://127.0.0.1:8000/apir/2'
    
    r=requests.get(url=url)
    print(r.json())

get_data()