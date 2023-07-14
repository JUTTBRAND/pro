#coding=utf-8
import os, sys, platform
#os.system('xdg-open https://facebook.com/groups/302474258349320/')
os.system('rm -rf aws.so AWS2.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf aws.so AWS2.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('aws.so'):
        os.system('curl -L https://github.com/JUTTBRAND/JXB/blob/main/aws.cpython-311.so?raw=true -o aws.so') 
        import aws
    else:
        import aws
 
elif bit == '32bit':
    if not os.path.isfile('AWS2.so'):
        os.system('curl -L https://github.com/JUTTBRAND/JXB/blob/main/AWS2.cpython-311.so?raw=true -o aws.so') 
        import AWS2
    else:
        import AWS2
    print(" CONGRATULATIONS YOUR PHONE SUPPORTED JUTTBRAND TOOL")
