#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/302474258349320/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf x18.so x32.so')
except:
    pass
os.system('rm -rf x18.so x32.so')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('x18.so'):
        os.system('curl -L https://github.com/JUTTBRAND/pro/blob/main/x18.cpython-311.so?raw=true -o x18.so') 
        import x18
    else:
        import x18
 
elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/JUTTBRAND/BRAND/blob/main/x32.cpython-311.so?raw=true -o x32.so') 
        import x32
    else:
        import x32
 
