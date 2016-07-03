import random
i=1
t=0
x=1
y=101
ds=0
s=0
sore=100
a=random.randrange(1,101)
print(a)
while sore>0:
    try:
        b=int(input("输入你猜的数[1-100]"))
    except:
        print("警告:请输入一个数字")
    if b in range(x,y):
        if b<a:
            x=b+1
            s+=1
            print("猜小了，提示：",x,"到",y)
          
        if b>a:
            y=b-1
            s+=1
            print("猜大了，提示：",x,"到",y)
        elif b==a:
            print("你猜对了")
            t=t+1
            break
 
    else:
        print("警告:请看提示，您将被加倍扣分")
        ds+=1;
    t=ds+s;
    sore=100-ds*4-2*s

else:
    print("您太笨了")
if sore<0:
    sore=0
print("您猜了 ",t,"次 ","被警告",ds,"次 ","分数：",sore)
