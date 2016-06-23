#! /usr/bin/env python
#-*- coding: utf-8 -*-

import time
#import subprocess as sub
import geomech

#ret6 = dome.start_dome_server()

ret0 = geomech.start_geomech_server()
ret1 = geomech.geomech_client('172.20.0.12',8100)

while(1):
    ret = ret1.get_geomech_col()
    geomech_col = ret1.read_geomech()
    tv = time.time()
    time.sleep(0.1)
