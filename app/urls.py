from handlers.helloworld import (
    HelloworldHandler,
    HelloworlRedisHandler
)

url_patterns = [
    (r"/?", HelloworldHandler),
    (r"/redis?", HelloworlRedisHandler),
]
