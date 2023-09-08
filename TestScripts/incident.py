import requests
import json

url = "https://dev179896.service-now.com/api/now/table/incident"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "Short_Description":"Short desc"
}

res = requests.post(url,auth = ("admin","yw^zW!SiUP26"),headers = headers, data = json.dumps(payload))

print(res.text)