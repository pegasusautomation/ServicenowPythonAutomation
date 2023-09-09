import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('devservicenow73@gmail.com','uljmyygvkgdhlnmj')

server.sendmail('suchiputti1@gmail.com', 'ga.rag9@gmail.com','Mail sent form python')

print('Mail Sent')