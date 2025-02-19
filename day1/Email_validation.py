# Email Validation with Regex
import re
def check(email):
    pattern = r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}$"
    return bool(re.match(pattern, email))

email=input("enter the email : ")
if check(email):
    print("email is  valid ")
else:
    print("email is not valid")