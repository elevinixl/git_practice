import re

def isStrongPassword(text):
    lengthRegex = re.compile(r'.{8}.*')
    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    numRegex = re.compile(r'\d')
    if lengthRegex.search(text) and upperRegex.search(text) and lowerRegex.search(text) and numRegex.search(text):
        return True
    else:
        return False

password = '1223423423aE3'
print(isStrongPassword(password))