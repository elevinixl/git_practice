import re

def regexStrip(text, remove = '\s'):
    removeRegex = re.compile(r'^('+remove+'*)(.*?)('+remove+'*)$')
    return removeRegex.search(text)[2]

text = '  asfd    '
print(regexStrip(text))

text = 'aaaEdLeavinaaa'
print(regexStrip(text,'a'))