import os
import sys
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# Create a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create a StreamHandler to print to stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

# Define a log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(stdout_handler)


# Configuration
port = "587"
smtp_server = "smtp.gmail.com"
login = "pavithresupprtfw1@gmail.com"
password = "alzfjobodjlnehfu"

sender_email = "pavithresupprtfw1@gmail.com"
receiver_emails = "pavithresupprtfw1@gmail.com,pavithrerathnayake@gmail.com,desmond.allon@gmail.com"

# print(receiver_emails.split(","))
receiver_emails_array = receiver_emails.split(",")
# print("Sending emails to: " + str(receiver_emails_array))
logger.info("Sending emails to: " + str(receiver_emails_array))

### Directory containing the images
image_directory = "screenshots"

### Dynamically gather all image paths from the directory
image_paths = [
    os.path.join(image_directory, file_name)
    for file_name in os.listdir(image_directory)
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
]
logger.info(list(reversed(image_paths)))

### Email content
subject = "HTML Email with Inline Image from modified"

## Generate dynamic HTML content with inline images
html_body = """\
<html>
  <body>
    <p>Hi,<br>
    This is a <b>Kibana</b> email with multiple inline images sent using Python.</p>
"""

## Dynamically add <img> tags for each image
for i in range(1, len(image_paths) + 1):
    html_body += f'<p><img src="cid:image{i}"></p>\n'

html_body += """\
  </body>
</html>
"""


### Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails_array)
message["Subject"] = subject
message.attach(MIMEText(html_body, "html"))

### Open the image files in binary mode and attach it
for i, img_path in enumerate(list(reversed(image_paths)), 1):
    with open(img_path, "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header("Content-ID", f"<image{i}>")
        message.attach(img)

### Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_emails_array, message.as_string())

logger.info("Email Sent!!!")