def YearRatio(dayRatio):
    #configure a year has 365 days
    ratio=pow(1+dayRatio,365)
    return ratio

dayRatio=float(input('Please input the dayRatio\n'))

yearRatio=YearRatio(dayRatio)

print('Your YearRatio is ',yearRatio)
