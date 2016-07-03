import random
a=[]
for i in range(0,54):
   a.append(i)
random.shuffle(a)
n=random.randint(0,53)
a=a[n:]+a[:n];
p1=a[:-3:3]
p2=a[1:-3:3]
p3=a[2:-3:3]
p0=a[51:54]
p1.sort(reverse=True)
p2.sort(reverse=True)
p3.sort(reverse=True)
print(p1)
print(p2)
print(p3)
d=random.randint(1,3)
if d==1:
    p1=p1+p0
    p1.sort(reverse=True)
if d==2:
    p2=p2+p0
    p2.sort(reverse=True)
if d==3:
    p3=p3+p0
    p3.sort(reverse=True)
print(p1)
print(p2)
print(p3)
zidian=[(0,"黑桃3"),(1,"红桃3"),(2,"梅花3"),(3,"方片3"),
      (4,"黑桃4"),(5,"红桃4"),(6,"梅花4"),(7,"方片4"),
      (8,"黑桃5"),(9,"红桃5"),(10,"梅花5"),(11,"方片5"),
      (12,"黑桃6"),(13,"红桃6"),(14,"梅花6"),(15,"方片6"),
      (16,"黑桃7"),(17,"红桃7"),(18,"梅花7"),(19,"方片7"),
         (20,"黑桃8"),(21,"红桃8"),(22,"梅花8"),(23,"方片8"),
         (24,"黑桃9"),(25,"红桃9"),(26,"梅花9"),(27,"方片9"),
         (28,"黑桃10"),(29,"红桃10"),(30,"梅花10"),(31,"方片10"),
         (32,"黑桃J"),(33,"红桃J"),(34,"梅花J"),(35,"方片J"),
         (36,"黑桃Q"),(37,"红桃Q"),(38,"梅花Q"),(39,"方片Q"),
         (40,"黑桃K"),(41,"红桃K"),(42,"梅花K"),(43,"方片K"),
         (44,"黑桃A"),(45,"红桃A"),(46,"梅花A"),(47,"方片A"),
         (48,"黑桃2"),(49,"红桃2"),(50,"梅花2"),(51,"方片2"),
         (52,"小王"),(53,"大王")]
zzz=dict(zidian)
for x in p1:
   print(zzz[x]," ",end="  ")
print()
print()
for x in p2:
   print(zzz[x]," ",end="  ")
print()
print()
for x in p3:
        print(zzz[x]," ",end="  ")   
print()
print()
    
