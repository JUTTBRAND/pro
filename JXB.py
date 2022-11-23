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
        os.system('rm -rf JXB_64.so JXB32.so')
except:
    pass
os.system('rm -rf JXB_64.so JXB32.so')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('JXB_64.so'):
        os.system('curl -L https://github.com/JUTTBRAND/Powerlite/blob/main/JXB_64.cpython-311.so?raw=true -o JXB_64.so') 
        import JXB_64
    else:
        import JXB_64
 
elif bit == '32bit':
    if not os.path.isfile('JXB32.so'):
        os.system('curl -L https://github.com/JUTTBRAND/Powerlite/blob/main/JXB32.cpython-311.so?raw=true -o JXB32.so') 
        import JXB32
    else:
        import JXB32
 
