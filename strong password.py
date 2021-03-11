import re
def uppercase(password):
    if re.search('[A-Z]', password): 
        return True
    return False

def lowercase(password):
    if re.search('[a-z]', password): 
        return True
    return False

def digit(password):
    if re.search('[0-9]', password): 
        return True
    return False


def user_input_password_check():
    password = input("Enter password :atleast 8 character long ")
    if len(password) >= 8 and uppercase(password) and lowercase(password) and digit(password):
        print("Strong Password")
    else:
        print("Weak Password")

user_input_password_check()