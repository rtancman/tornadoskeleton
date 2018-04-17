#!/usr/bin/env python
import sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from settings import settings
from urls import url_patterns


logger = logging.getLogger('tornadoskeleton')


class App(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(
            self, url_patterns, **settings)


def main():
    app = App()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(settings['port'], settings['host'])

    try:
        logger.info(
            'app running at {}:{}'.format(settings['host'], settings['port']))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.stdout.write('app closed by user interruption')
        sys.stdout.write('\n')


if __name__ == "__main__":
    main()
