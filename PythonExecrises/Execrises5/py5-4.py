def leapYear(year):
    Y=int(year)
    if (Y%4==0 and Y%100!=0) or (Y%400==0):
        return True
    else:
        return False

year=input('Please input a leap year\n')

if leapYear(year):
    print('This is a leap year!\n')
else:
    print('This is not a leap year.\n')
