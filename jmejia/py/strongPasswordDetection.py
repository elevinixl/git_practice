import re

# At least 8 characters long
# Contains uppercase letters
# Contains lowercase letters
# Contains numbers

def isStrongPassword(text):
    longRE = re.compile(r'.{8}')
    upperRE = re.compile(r'[A-Z]')
    lowerRE = re.compile(r'[a-z]')
    digitRE = re.compile(r'\d')

    if longRE.search(text) and upperRE.search(text) and lowerRE.search(text) and digitRE.search(text):
        return True
    else:
        return False

print(isStrongPassword('elloABC1'))