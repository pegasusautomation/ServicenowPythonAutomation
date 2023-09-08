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

res = requests.get(url,auth = ("admin","yw^zW!SiUP26"),headers = headers, data = json.dumps(payload))
psrsedData = res.json()
for json_inner_data in psrsedData['result']:
        print(json_inner_data['number'] + " Updated on Date: " + json_inner_data['sys_updated_on'])
print("Total Number Of Incedents: " + str(len(psrsedData['result'])))