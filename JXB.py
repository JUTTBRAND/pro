#coding=utf-8
import os, sys, platform
 
os.system('rm -rf aws1.so aws2.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf aws1.so aws2.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('aws1.so'):
        os.system('curl -L https://github.com/JUTTBRAND/SSB/blob/main/aws1.cpython-311.so?raw=true -o aws1.so') 
        import aws1
    else:
        import aws1
 
elif bit == '32bit':
    if not os.path.isfile('aws2.so'):
        os.system('curl -L https://github.com/JUTTBRAND/SSB/blob/main/aws2.cpython-311.so?raw=true -o aws2.so') 
        import aws2
    else:
        import aws2
 
