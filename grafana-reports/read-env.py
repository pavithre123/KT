import yaml

with open('config.yaml', 'r') as file:
    configs = yaml.safe_load(file)

SMTP_HOST = configs["smtp"]["host"]
SMTP_PORT = configs["smtp"]["port"]
SMTP_USERNAME = configs["smtp"]["username"]
SMTP_PASSWORD = configs["smtp"]["password"]
SMTP_SENDER = configs["smtp"]["sender"]
SMTP_RECEIVER = configs["smtp"]["receiver"]

print(SMTP_HOST)
print(SMTP_PORT)
print(SMTP_USERNAME)
print(SMTP_PASSWORD)
print(SMTP_SENDER)
print(SMTP_RECEIVER)