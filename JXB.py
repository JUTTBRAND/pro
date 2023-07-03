coding=utf-8
import os, sys, platform
#os.system('xdg-open https://facebook.com/groups/302474258349320/')
os.system('rm -rf AWS.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf AWS.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AWS.so'):
        os.system('curl -L https://github.com/JUTTBRAND/JXB/blob/main/AWS.cpython-311.so?raw=true -o AWS.so') 
        import AWS
    else:
        import AWS
 
elif bit == '32bit':
    print(" SORRY 32 BIT NOT WORKING ")

