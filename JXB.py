#coding=utf-8
import os, sys, platform
os.system('xdg-open https://facebook.com/groups/302474258349320/')
os.system('rm -rf aws1.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf JXB.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('JXB.so'):
        os.system('curl -L https://github.com/JUTTBRAND/SSB/blob/main/JXB.cpython-311.so?raw=true -o JXB.so') 
        import JXB
    else:
        import JXB
 

  
