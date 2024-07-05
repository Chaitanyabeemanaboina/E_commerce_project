import requests

BASE_URL = 'http://127.0.0.1:8000/api/'
def jwt_token():
    ENDPOINT = 'token/'
    cred_details = {
        'username':'chaitanya',
        'password':'aaa1111'
    }
    response = requests.post(BASE_URL + ENDPOINT,json=cred_details)
    return response

ENDPOINT = 'token/'
cred_details = {
            'username':'chaitanya',
            'password':'aaa1111'
}
response = requests.post(BASE_URL + ENDPOINT,json=cred_details)
auth_response = response.json()
access_token = auth_response['access']
token = 'Bearer'+ ' ' + f'{access_token}'
headers = {'Authorization' : str(token),
               }
BASE_URL_api = 'http://127.0.0.1:8000/api/'
ENDPOINT_api = 'api-key/'
resp = requests.post(BASE_URL_api + ENDPOINT_api, headers=headers)
headers1 = {'Authorization' : str(token),
               'X-API-KEY':resp.json()['key']
               }
def list_api():
    ENDPOINT_LIST = 'listapi/'
    resp = requests.get(BASE_URL + ENDPOINT_LIST, headers=headers1)
    return resp
# # list()
def post():
    ENDPOINT_POST = 'createapi/'
    post_dict = {
        'name':'Lenin Shirts',
        'prize':1500,
        'quantity':0,
        'category':'Cloths',
        'bill':False,
        'add_to_cart':False
    }
    resp = requests.post(BASE_URL+ENDPOINT_POST,headers=headers1,json=post_dict)
    return resp
# post()
def update():
    ENDPOINT_UPD = 'updateapi/55'
    updt_dict = {
        'name': 'Lenin Shirts',
        'prize': 1500,
        'category': 'Cloths',
    }
    resp = requests.put(BASE_URL + ENDPOINT_UPD, headers=headers1, json=updt_dict)
    return resp
# update()
def delete():
    ENDPOINT_DLT = 'destroyapi/52'
    resp = requests.delete(BASE_URL + ENDPOINT_DLT, headers=headers1)
    return resp



#TO GENERATE API KEY:
def api_key():
    BASE_URL_api = 'http://127.0.0.1:8000/api/'
    ENDPOINT_api = 'api-key/'
    resp = requests.post(BASE_URL_api+ENDPOINT_api,headers=headers)
    return resp

