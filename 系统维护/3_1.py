import os,glob,shutil
'''#(1)
pathlist=[r'd:\ptest']
a=open('e:\log.txt','w')
a.write('格式一\n')
for (d,s,f) in os.walk(pathlist[0]):
    i="-----------------------------------------------\r\n"
    a.write(i)
    j='['+d+']'
    a.write(j)
    a.write('\n')
    for fsub in s:
        i='[folder]:'+fsub
        a.write(i)
        a.write('\n')
    for fname in f:
        j='[file]:'+fname
        a.write(j)
        a.write('\n')
a.close()'''

#os.path.join(dirname,i))
#os.chdir("d:\\ptest")
'''ATTRIB [+R | -R] [+A | -A ] [+S | -S] [+H | -H] [+I | -I]
#       [drive:][path][filename] [/S [/D] [/L]]
#  + 设置属性。
#  - 清除属性。
#  R 只读文件属性。
#  A 存档文件属性。
#  S 系统文件属性。
#  H 隐藏文件属性。
#  I 无内容索引文件属性。
#  [drive:][path][filename]
#      指定 attrib 要处理的文件。
#  /S 处理当前文件夹及其所有子文件夹中的匹配文件。
#  /D 也处理文件夹。
  /L 处理符号链接和符号链接目标的属性。
'''
#（2）修改files文件夹中的notepad.exe的文件属性为只读、隐藏。
os.chdir(r'd:\ptest\files')
os.popen(r'attrib  notepad.exe  +R +H')
print("--------设置成功------") 
#（3）重命名文件夹temp为mytemp。
os.chdir(r'd:\ptest\files')
os.popen(r'ren temp mytemp')
#(4)查找ptest（包含子目录）下的所有的隐藏文件及文件夹，并将它们以全路径方式存储在log.txt文件中。
os.chdir(r'd:\ptest')
pathlist=[r'd:\ptest']
for(d,s,files) in os.walk(pathlist[0]):
#    pathlist.append(os.path.join(dirname,i))
    for i in s:
        pathlist.append(os.path.join(d,i))
    for i in files:
        pathlist.append(os.path.join(d,i))
#print(pathlist)
for i in pathlist:
    print(i)
    
