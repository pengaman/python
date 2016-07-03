
class computer:   
     def __init__(self,changshang,name,ip):
          self.__cpu=[0,0]
          self.__neicun=0
          self.__yingpan=0
          self.changshang=changshang
          self.name=name
          self.ip=ip
     def setcpu(self,cpu1,cpu2):
          if cpu1>0 and cpu2>0:
               self.__cpu.append(cpu1)
               self.__cpu.append(cpu2)
          else:
               print("输入不合法")
     def setneicun(self,neicun):
          try:
               if int(neicun)==float(neicun) and neicun>0:
                    self.__neicun=neicun
               else:
                    print("输入不合法")
          except:
               print("输入的不是数字")
     def setyingpan(self,yingpan):
          try:
               if int(yingpan)==float(yingpan) and yingpan>0:
                    self.__yingpan=yingpan
               else:
                    print("输入不合法")
          except:
               print("输入的不是数字")
     def getcpu(self):
          return self.__cpu[0],self.__cpu[1]
     def getneicun(self):
          return self.__neicun
     def getyingpan(self):
          return self.__yingpan
     def shuchucpu(self):
          if self.__cpu==[]:
               print("未设置cpu")
          else:
               x,y=self.getcpu()
               print(str(x)+"核"+str(y)+"G")
     def shuchuneicun(self):
          if self.__neicun==0:
               print("未设置内存")
          else:
               x=self.getneicun()
               if self.__neicun>80:
                    print(str(x)+"M")
               else:
                    print(str(x)+"G")
               print(str(x)+"核"+str(y)+"G")
     def shuchuyingpan(self):
          if self.__yingpan==0:
               print("未设置硬盘")
          else:
               r=self.getyingpan()
               print(str(r)+"G")
c1=computer("hp","hp1","192.168.1.1")
c1.shuchucpu()
c1.setcpu(7,9)
c1.shuchucpu()
c1.shuchuyingpan()


          
