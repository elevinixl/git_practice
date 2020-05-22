import re

def dateDetection(text):
    dumbDateRE = re.compile(r'(\d\d)/(\d\d)/(\d{4})')
    avgDateRE = re.compile(r'([0-3]\d)/([01]\d)/([12]\d{3})')
    smartDateRE = re.compile(r'([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})')



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