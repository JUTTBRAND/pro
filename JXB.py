#coding=utf-8
import os, sys, platform
os.system('xdg-open https://facebook.com/groups/302474258349320/')
os.system('rm -rf aws1.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf aws1.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('aws1.so'):
        os.system('curl -L https://github.com/JUTTBRAND/JXB/blob/main/aws1.cpython-311.so?raw=true -o aws1.so') 
        import aws1
    else:
        import aws1
 

    print(" CONGRATULATIONS YOUR PHONE SUPPORTED JUTTBRAND TOOL")
