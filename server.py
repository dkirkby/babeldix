#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

from __future__ import division,print_function

import SocketServer

def main():
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

if __name__ == '__main__':
    main()
