import pandas as pd


class writeIncidentListToXl:
        def writeDataToXl(incident_List,Incident_Assigned_Group):
                path = "E:\GA - Dont Delete\ServicenowPythonAutomation\Test_Data\Incident_List.xlsx"
                df = pd.DataFrame(list(zip(incident_List,Incident_Assigned_Group)),columns=["incident_List","Incident_Assigned_Group"]).rename(columns={"Unnamed: 0":"Sl No"})
                df.to_excel(path)