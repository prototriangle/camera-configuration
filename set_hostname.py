#! /usr/bin/env python3
from dvrip import DVRIPCam
from time import sleep
from sys import argv

machine_name_key = 'General.General.MachineName'
hostname_key = 'NetWork.NetCommon.HostName'


if len(argv) < 3:
    print('Please provide IP of camera and hostname as arguments')
    exit(2)

try:
    cam = DVRIPCam(argv[1], user='admin', password='54321')
    if cam.login():
        print('Login successful!')
    else:
       print('Login failed')
       exit(1)
    print('Setting hostname', end='...', flush=True)
    cam.set_info(machine_name_key, argv[2])
    sleep(1)
    cam.set_info(hostname_key, argv[2])
    sleep(1)
    print('done')
    print('Checking:')
    print(machine_name_key, cam.get_info(machine_name_key))
    print(hostname_key, cam.get_info(hostname_key))
    cam.close()
except:
    print('Something went wrong')
    exit(1)
