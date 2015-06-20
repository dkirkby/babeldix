#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

from __future__ import division,print_function

import socket
import json

import babeldix


def get_frame(sock):
    frame = ''
    while frame == '' or frame[-1] != '\n':
        frame += sock.recv(1024)
    return json.loads(frame[:-1])

def send_frame(sock, frame):
    sock.sendall(json.dumps(frame) + '\n')

def take_challenge(sock, command, responder):
    send_frame(sock, command)
    challenge = get_frame(sock)
    print('challenge: {}'.format(challenge))
    response = responder.get_response(challenge)
    print('response: {}'.format(response))
    send_frame(sock, response)
    answer = get_frame(sock)
    print('answer: {}'.format(answer))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect(('localhost', 1234))
        # Take a challenge.
        #take_challenge(sock, 'hello', babeldix.Hello)
        #take_challenge(sock, 'histogram', babeldix.Histogram)
        #take_challenge(sock, 'circles', babeldix.Circles)
        take_challenge(sock, 'plates', babeldix.Plates)
    finally:
        sock.close()

if __name__ == '__main__':
    main()
