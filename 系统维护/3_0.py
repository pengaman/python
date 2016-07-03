import shutil
import os,glob
os.mkdir(r'd:\ptest')
os.mkdir(r'd:\ptest\document')
os.mkdir(r'd:\ptest\files')
os.mkdir(r'd:\ptest\temp')
a=list(glob.glob(r'c:\windows\*.ini'))
for i in a:
    shutil.copy(i,r'd:\ptest\document')
c=list(glob.glob(r'c:\windows\n*'))
for i in c:
    shutil.copy(i,r'd:\ptest\files')

a=os.path.exists(r'd:\ptest\files\notepad.exe')
if a:
    shutil.copy(r'd:\ptest\files\notepad.exe',r'd:\ptest\temp\mypad.exe')
a=os.path.exists(r'd:\ptest\document\win.ini')
if a:
    shutil.move(r'd:\ptest\document\win.ini',r'd:\ptest\temp')
a=os.path.exists(r'd:\ptest\document\system.ini')
if a:
    shutil.copy(r'd:\ptest\document\system.ini',r'd:\ptest\temp\system.inf')
    os.remove(r'd:\ptest\document\system.ini')
os.mkdir(r'd:\ptest\document\mydir')
a=list(glob.glob(r'd:\ptest\temp\*'))
for i in a:
    shutil.copy(i,r'd:\ptest\document\mydir')
shutil.copytree(r'd:\ptest\files',r'd:\ptest\document\mydir\myfiles')
shutil.rmtree(r'd:\ptest\files')

