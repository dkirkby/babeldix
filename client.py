#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

from __future__ import division,print_function

import socket
import json


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect(('localhost', 1234))
        sock.sendall('hello\n')

        # Receive data from the server and shut down
        received = json.loads(sock.recv(1024))
        print('received: {}'.format(received))

    finally:
        sock.close()

if __name__ == '__main__':
    main()
