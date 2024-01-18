import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Kodētas rēķinu lapas"
body = "Labdien,\nPielikumā ir pievienots Excel fails ar kodēto pavadzīmju informāciju.\nAr cieņu,\nRoberts Helmanis"
sender_email = str(input("Ievadiet e-pastu no kura sūtīt ziņojumu: "))
receiver_email = str(input("Ievadiet e-pastu uz kuru sūtīt ziņojumu: "))
password = str(input("Ievadiet SMTP paroli: "))

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

filename = "Kodetie_dati.xlsx"

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.inbox.lv", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

print("E-pasta ziņojums ir nosūtīts!")