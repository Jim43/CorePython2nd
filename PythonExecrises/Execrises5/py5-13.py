def hour2minute(time):
    s=time.split('.')
    return int(s[0])*60+int(s[1])

time=input('please input a hour number(eg:2.3)\n')

minutes=hour2minute(time)

print('the total mimutes is ',minutes)

