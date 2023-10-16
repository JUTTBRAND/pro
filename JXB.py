#coding=utf-8
import os, sys, platform
 
os.system('rm -rf aws1.so aws32.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf aws1.so aws32.so')
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
    if not os.path.isfile('aws32.so'):
        os.system('curl -L https://github.com/JUTTBRAND/SSB/blob/main/aws32.cpython-311.so?raw=true -o aws32.so') 
        import aws32
    else:
        import aws32
 
 
