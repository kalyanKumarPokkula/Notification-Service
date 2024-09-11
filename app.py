import json
import redis
import requests
import smtplib
from email.mime.text import MIMEText

# subject = "Email Subject"
# body = "This is the body of the text message"
# sender = "sender@gmail.com"
# recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]
# password = "password"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = recipients
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# send_email(subject, body, sender, recipients, password)




redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

url = "http://localhost:3000/api/send_order_confirmation"
while True:
    try:
        message = redis_client.rpop("message_queue")
        data = json.loads(message)
        print(data)
        if data:
            response = requests.post(url , json=data)
            print(response.status_code)
    except Exception as e:
        pass