#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

from __future__ import division,print_function

import SocketServer
import threading
import logging
import json
import pprint
import timeit

import babeldix


tasks = {
    'hello': babeldix.Hello(),
    'histogram': babeldix.Histogram(num_values=100, bin_size=3, num_bins= 10),
    'circles': babeldix.Circles(min_circles=4, max_circles=6),
}

class Handler(SocketServer.StreamRequestHandler):

    def send(self,message):
        line = json.dumps(message, separators=(',',':'))
        logging.debug('[{}] SENDING >>{}<<'.format(self.client_address[1],line))
        self.wfile.write(line + '\n')

    def receive(self):
        line = self.rfile.readline().strip()
        if line == '':
            logging.warn('[{}] DISCONNECTED'.format(self.client_address[1]))
            return None
        logging.debug('[{}] RECEIVED >>{}<<'.format(self.client_address[1],line))
        try:
            message = json.loads(line)
            formatted = pprint.pformat(message, indent=2, depth=4)
            logging.info('[{}] PARSED:\n{}'.format(self.client_address[1], formatted))
            return message
        except ValueError as e:
            logging.warn('[{}] PARSE ERROR'.format(self.client_address[1]))
            return None

    def handle(self):
        port = self.client_address[1]
        logging.info('[{}] CONNECTED'.format(port))
        command = self.receive()
        if command in tasks:
            task = tasks[command]
            challenge = task.get_challenge()
            answer = task.get_response(challenge)
            start_time = timeit.default_timer()
            self.send(challenge)
            response = self.receive()
            stop_time = timeit.default_timer()
            elapsed = stop_time - start_time
            if task.is_correct(response, answer):
                self.send('yes')
                logging.info('[{}] CORRECT IN {:.3f}s'.format(port,elapsed))
            else:
                self.send('no')
        else:
            self.send('error')

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s # %(message)s')
    server = ThreadedTCPServer(('localhost', 1234), Handler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    logging.info('Server v{} listening at {}...'.format(
        babeldix.__version__,server.server_address))
    try:
        while True:
            pass
    except KeyboardInterrupt as e:
        print('bye')
    finally:
        server.shutdown()
        logging.info('Server shutdown.')

if __name__ == '__main__':
    main()
