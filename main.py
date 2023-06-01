#least square fitting
n=(input('enter how many pair of x and y'))
sx=0
sy=0
sxy=0
sx2=0
for i in range (1,n+1):
    print('enter x',i)
    print('enter y',i)
    x=float(input())
    y=float(input())
    sx=sx+x
    sy=sy+xm
    sxy=sxy+(x*y)
    sx2=sx2+(x**2)
    m=(sx*sy-n*sxy)/(sx*sx-n*sx2)
    c=(sx2*sy-sxy*sx)/(n*sx2-sx**2)
    print('slope is %5.3f% m')
    print('intercept is %5.3f% c')
