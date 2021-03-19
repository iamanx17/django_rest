import requests
import json



def get_data(id=None):    
    url='http://127.0.0.1:8000/'
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=url, data=json_data) #it will give Response [500] or.....
    print(r.json())


def post_data():
    url="http://127.0.0.1:8000/studentpost/"
    data={
        'name':'Kishan',
        'roll':31402,
        'city':'jaunpur',
    }
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)

post_data()

