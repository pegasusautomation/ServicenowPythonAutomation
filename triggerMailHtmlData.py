from email.message import EmailMessage
import smtplib
from getAllIncidents import getAllIncidents
import json
import pandas as pd

file = open("credentials.json")
data = json.load(file)
# define content
recipients = data["recieveremail"]
sender = data["senderemail"]
senderpassword = data["senderpassword"]
subject = "Mail sent by python code written by RAGHAVENRDRA G A"
list = getAllIncidents.getincidentapi()

#To write list of text into text doc
with open ('text.txt', 'w') as file:  
    for line_1 in list:  
        file.write(line_1)  
        file.write('\n') 
#Read file data using pandas
data = pd.read_csv("text.txt",sep=" ")
pd.set_option("display.max_rows",200)
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
    data
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