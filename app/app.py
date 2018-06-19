#!/usr/bin/env python
import sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import aioredis
import asyncio
from settings import SETTINGS, CACHE
from urls import url_patterns


logger = logging.getLogger('tornadoskeleton')


class App(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(
            self, url_patterns, **SETTINGS)

    def init_with_loop(self, loop):
        self.redis = loop.run_until_complete(
            aioredis.create_redis(
                (CACHE['default']['host'], CACHE['default']['port']),
                loop=loop
            )
        )


def main():
    app = App()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(SETTINGS['port'], SETTINGS['host'])

    try:
        logger.info(
            'app running at {}:{}'.format(SETTINGS['host'], SETTINGS['port']))
        loop = asyncio.get_event_loop()
        app.init_with_loop(loop)
        loop.run_forever()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.stdout.write('app closed by user interruption')
        sys.stdout.write('\n')


if __name__ == "__main__":
    main()
