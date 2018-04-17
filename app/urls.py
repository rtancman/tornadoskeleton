from handlers.helloworld import HelloworldHandler

url_patterns = [
    (r"/?", HelloworldHandler),
]
