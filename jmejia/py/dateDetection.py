import re

def dateDetection(text):
    dumbDateRE = re.compile(r'(\d\d)/(\d\d)/(\d{4})')
    avgDateRE = re.compile(r'([0-3]\d)/([01]\d)/([12]\d{3})')
    smartDateRE = re.compile(r'(0[1-9]|[1-2]\d|3[01])/(0[1-9]|1[0-2])/([12]\d{3})')

    matches = smartDateRE.findall(text)
    dates = []
    for day,month,year in matches:
        if month == '02':
            if int(day) > 29:
                continue
            elif int(day) < 29:
                dates.append('/'.join([day,month,year]))
            elif int(year) % 4:
                continue
            elif int(year) % 100:
                dates.append('/'.join([day, month, year]))
            elif int(year) % 400:
                continue
            else:
                dates.append('/'.join([day, month, year]))
        elif month in ['04','06','09','11']:
            if int(day) > 30:
                continue
            else:
                dates.append('/'.join([day, month, year]))
        else:
            dates.append('/'.join([day, month, year]))
    return dates

message = 'Pi Day is on 14/03/2000 in the US, but is approximately on 22/07/2020 in the UK.  Tau Day is on 28/06/2020 in the US.'

for date in dateDetection(message):
    print('Date found: ' + date)


# DD/MM/YYYY  (British dates)
# days range 01-31
# months range 01-12
# years range 1000-2999
# days and months use leading 0s (always 2 digits)
# correct days for months don't matter (don't need to be a calendar)

# store DD, MM, YYYY into day, month, year
# regex doesn't need to check for valid day/month/year (combo of regex and logic checks)
# April, June, September, November: 30 days
# February: 28 days (29 on leap years)
# Jan/March/May/July/Aug/Oct/Dec: 31 days

# leap years are divisible by 4, unless divisible by 100, unless divisible by 400