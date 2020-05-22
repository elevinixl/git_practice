import re

def dateDetection(text):
    dateRegex = re.compile(r'''
        (0[1-9]|[12]\d|30|31)   #day
        /
        (0[1-9]|1[0-2])         #month
        /
        ([12]\d{3})             #year
        ''',re.VERBOSE)

    for date in dateRegex.findall(text):
        day = date[0]
        month = date[1]
        year = date[2]

        if day == '31' and month in ['02','04','06','09','11']:
            print('/'.join(date) + ' is not a real date!')
            continue
        elif day == '30' and month == '02':
            print('/'.join(date) + ' is not a real date!')
            continue
        elif day == '29' and month == '02':
            if int(year) % 4 != 0:
                print('/'.join(date) + ' is not a real date!')
                continue
            elif int(year) % 100 == 0 and int(year) % 400 != 0:
                print('/'.join(date) + ' is not a real date!')
                continue
        print('/'.join(date) + ' is a real date.')

foo = '1d/02/1990 23/01/1933 29/02/2000 29/02/2001 29/02/2004 29/02/2100'
dateDetection(foo)