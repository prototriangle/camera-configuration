#! /bin/bash
IP='10.0.0.12'
HOSTNAME='BatBox1'
TITLE='Bat Camera 1'

./update_time.py "$IP"
./move_text_to_bottom.py "$IP"
./set_name.py "$IP" "$TITLE"
./set_hostname.py "$IP" "$HOSTNAME"

./list_cams.py
