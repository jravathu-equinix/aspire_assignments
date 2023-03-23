import re

email_list = ["ravathu.jahnavi*^&@gmail.com", "123ravathujahnavi@gmail.com", "ravathu123jahnavi@gmail.com", "12$&**3ravathu2001jahnavi@gmail.com"]

def getDetails(list):
    for email in email_list:
        details = email.split("@")
        user_name = re.sub(r'[^a-zA-Z]','', details[0])    
        domain_name = details[1][:details[1].find(".")]
        print("User Name:",user_name, "    Domain Name:",domain_name)

getDetails(email_list)