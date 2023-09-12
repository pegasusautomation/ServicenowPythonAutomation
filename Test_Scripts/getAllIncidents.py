import requests
import json
class getAllIncident:
 def __init__(self) -> None:
     pass
 
 def getincidentapi():
        listOfIncidents = []
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
        for item in psrsedData['result']:
            listOfIncidents.append(item['number'])
        return listOfIncidents
            # print(listOfIncident)
# with open ('text.txt', 'w') as file:  
#              for line_1 in listOfIncident:  
#                  file.write(line_1)  
#                  file.write('\n')
            # print(listOfIncident['number'] + " Updated on Date: " + listOfIncident['sys_updated_on'])
        # print("Total Number Of Incedents: " + str(len(psrsedData['result'])))