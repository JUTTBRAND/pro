#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

os.system('xdg-open https://facebook.com/groups/302474258349320/')

os.system('git pull')

 

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('x18.cpython-311.so'):

        os.system('curl -L https://github.com/JUTTBRAND/pro/blob/main/x18.cpython-311.so?raw=true') 

    import x18

    x18.run()

 

elif bit == '32bit':

    if not os.path.isfile('x1832.cpython-311.so'):

        os.system('curl -L https://github.com/JUTTBRAND/pro/blob/main/x1832.cpython-311.so?raw=true') 

    import x1832

    x1832.run()

