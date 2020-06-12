import re

def reStrip(text, ch=''):
    if ch == '':
        stripRE = re.compile(r'^ *(.*?) *$')
        return stripRE.search(text).group(1)
    else:
        stripRE = re.compile(ch)
        return stripRE.sub('', text)

message = '  what  have we      here  '

print('[' + reStrip(message, 'h') + ']')