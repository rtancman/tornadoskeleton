import tornado.web


class HelloworldHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(200)
        self.write('OK')

class HelloworlRedisHandler(tornado.web.RequestHandler):
    async def get(self):
        redis = self.application.redis
        await redis.set('my-key', 'OK')
        val = await redis.get('my-key')
        self.set_status(200)
        self.write('Hello asyncio redis: {}'.format(val))
