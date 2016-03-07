# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 13:58:10 2016
@author: tkabelan
"""

import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4inf.com', 80))

#mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
mysocket.send('GET http://www.publications.parliament.uk/pa/bills/lbill/2015-2016/0056/en/16056en01.htm HTTP/1.0\n\n')

while True:
    data = mysocket.recv(650)
    if (len(data) < 1):
        break
    print data
    
mysocket.close()