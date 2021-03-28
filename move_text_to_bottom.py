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

    print('Getting video widget info', end='...', flush=True)
    info = cam.get_info('AVEnc.VideoWidget')
    if info is not None:
        print('done')
    info[0]['ChannelTitleAttribute']['RelativePos'] = [128, 8192, 0, 0]
    info[0]['TimeTitleAttribute']['RelativePos'] = [8192, 8192, 0, 0]
    print('Setting video widget info', end='...', flush=True)
    cam.set_info('AVEnc.VideoWidget', info)
    sleep(1)
    print('done')
    cam.close()
except:
    print('Something went wrong')
    exit(1)
