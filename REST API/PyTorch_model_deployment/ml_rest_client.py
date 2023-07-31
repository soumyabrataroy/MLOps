import json
import requests

url = 'http://35.232.73.15:8005/model'

request_data = json.dumps({'age':42,'salary':20000})
response = requests.post(url,request_data)
print (response.text)



