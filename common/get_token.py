import requests
import getpass

def get_token(username=None,password=None): 
    print("--------Login to themap---------")
    if username == None:
        username = input("Enter username: ")
    if password == None:
        password = getpass.getpass('Password:')
    payload = {'grant_type':'password', 'userName' : username, 'password' : password}
    r = requests.post('https://auth.themap.net/Token', data = payload)
    json = r.json()
    return json['access_token']