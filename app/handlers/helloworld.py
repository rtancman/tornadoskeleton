import tornado.web


class HelloworldHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(200)
        self.write('OK')
