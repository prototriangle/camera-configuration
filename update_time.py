#! /usr/bin/env python3
from dvrip import DVRIPCam
from time import sleep
from sys import argv

if len(argv) < 2:
    print('Please provide IP of camera as argument')
    exit(2)

try:
    cam = DVRIPCam(argv[1], user='admin', password='54321')
    if cam.login():
        print('Login successful!')
    else:
       print('Login failed')
       exit(1)
    cam.set_time()
    sleep(1)
    cam.close()
except:
    print('Something went wrong')
    exit(1)
