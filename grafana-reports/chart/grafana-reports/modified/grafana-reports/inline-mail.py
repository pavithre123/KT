import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Configuration
port = "{{ .Values.grafanaReport.smtp.port }}"
smtp_server = "{{ .Values.grafanaReport.smtp.host }}"
login = "{{ .Values.grafanaReport.smtp.username }}"
password = "{{ .Values.grafanaReport.smtp.password }}"

sender_email = "{{ .Values.grafanaReport.smtp.sender }}"
receiver_email = "{{ .Values.grafanaReport.smtp.receiver }}"

# Email content
subject = "HTML Email with Inline Image from modified"
html = """\
<html>
  <body>
    <p>Hi,<br>
    This is a <b>test</b> email with an inline image sent using Python.</p>
    <p><img src="cid:image1"></p>
  </body>
</html>
"""

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the HTML part
message.attach(MIMEText(html, "html"))

# Open the image file in binary mode and attach it
# with open("/home/pavithra-121252/Documents/sre/Support/week-3/ss/dashboard_area.png", "rb") as img_file:
with open("/grafana-reports/scripts/dashboard_area.png", "rb") as img_file:
    img = MIMEImage(img_file.read())
    img.add_header("Content-ID", "<image1>")
    message.attach(img)

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')