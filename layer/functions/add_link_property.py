import requests

def add_link_property(link,name,value,token):
    headers = {'authorization': 'Bearer '+token}
    print("Adding property :"+ name)
    params ={
        "linkID" : link["ID"],
        "name" : name,
        "value" : value
    }
    r = requests.get('https://api.themap.net/api/Tour2/AddLinkProperty', params = params, headers = headers)
    return r.json()
