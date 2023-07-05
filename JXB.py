#coding=utf-8
import os, sys, platform
#os.system('xdg-open https://facebook.com/groups/302474258349320/')
os.system('rm -rf aws.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf aws.so')
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
    print(" SORRY 32 BIT NOT WORKING ")

