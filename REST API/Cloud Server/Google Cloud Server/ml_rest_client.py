import json
import requests

url = 'http://104.197.179.255:8006/model' # need to change the ip based on cloud server ip

request_data = json.dumps({'age':50,'salary':20000})
response = requests.post(url,request_data)
print (response.text)



