#!/usr/bin/env python
import sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from SETTINGS import SETTINGS
from urls import url_patterns


logger = logging.getLogger('tornadoskeleton')


class App(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(
            self, url_patterns, **SETTINGS)


def main():
    app = App()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(SETTINGS['port'], SETTINGS['host'])

    try:
        logger.info(
            'app running at {}:{}'.format(SETTINGS['host'], SETTINGS['port']))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.stdout.write('app closed by user interruption')
        sys.stdout.write('\n')


if __name__ == "__main__":
    main()
