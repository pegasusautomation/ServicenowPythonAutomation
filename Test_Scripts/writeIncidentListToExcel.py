import pandas as pd

class writeIncidentListToXl:
        def writeDataToXl(incident_List):
                path = "E:\GA - Dont Delete\ServicenowPythonAutomation\Test_Data\Incident_List.xlsx"
                df = pd.DataFrame(list(zip(incident_List))).add_suffix('Incident_List', None)
                df.to_excel(path)