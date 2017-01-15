pi=3.14

def squareArea(a):
    a=float(a)
    return a**2

def roundArea(a):
    a=float(a)
    return a**2*pi

def cubeVolume(a):
    a=float(a)
    return a**3

def ballVulume(a):
    a=float(a)
    return a**3*(4/3)*pi

select=int(input('Please choose a type:\n1.squareArea\n2.roundArea\n3.cubeVolume\n4.ballVulume\n'))

side=input('Please input the side length\n')

if select==1:
    result=squareArea(side)

elif select==2:
    result=roundArea(side)

elif select==3:
    result=cubeVolume(side)

elif select==4:
    result=ballVulume(side)

print('The result is ',result)
