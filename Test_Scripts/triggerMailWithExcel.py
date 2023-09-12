import smtplib
import json
import pandas as pd
from email.message import EmailMessage
from pretty_html_table import build_table
from getAllIncidents import getAllIncident
from writeIncidentListToExcel import writeIncidentListToXl

#Read credentials to send mail
file = open("credentials.json")
data = json.load(file)

# define content
recipients = data["recieveremail"]
sender = data["senderemail"]
senderpassword = data["senderpassword"]
subject = "Mail sent by python code written by RAGHAVENRDRA G A"
incident_List = getAllIncident.getincidentapi()

#To write list of text into excel doc
writeIncidentListToXl.writeDataToXl(incident_List)

#Read file data using pandas
path = "E:\GA - Dont Delete\ServicenowPythonAutomation\Test_Data\Incident_List.xlsx"
data = pd.read_excel(path)

# pd.set_option("display.max_rows",200)
print(data)
body = """
<html>
<head>
</head>


<body>
Hi All,
<br></br>

Please find the below incident list 

<br></br>
     {0}
</body>

</html>
""".format(
    build_table(
        data,
        "blue_light",
        width="auto",
        font_family="Open Sans",
        font_size="13px",
        text_align="justify",
    ),
)

# make up message
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender
msg["To"] = recipients
msg.add_alternative(body,subtype = "html")

# sending
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender, senderpassword)
send_it = session.sendmail(sender, recipients, msg.as_string())
session.quit()