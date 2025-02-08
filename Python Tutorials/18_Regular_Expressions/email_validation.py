import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

emails = ["user@example.com", "invalid-email@", "user.name@domain.com", "user@domain.co.in"]

for email in emails:
    print(f"{email}: {validate_email(email)}")


#output
# user@example.com: True
# invalid-email@: False
# user.name@domain.com: True
# user@domain.co.in: True