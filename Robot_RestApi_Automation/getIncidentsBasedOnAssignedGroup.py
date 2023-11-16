import requests
import json
class getAllIncidentWithAssignedGroups:
 
 def getincidentWithAssignedGroupApi():
        listOfIncidents = []
        listOfIncidentsWithAssignedGroup = []
        url = "https://dev176532.service-now.com/api/now/table/incident?sysparm_query=assignment_group=d625dccec0a8016700a222a0f7900d06"

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
            listOfIncidentsWithAssignedGroup.append(item['sys_updated_by'])
        return listOfIncidents,listOfIncidentsWithAssignedGroup
