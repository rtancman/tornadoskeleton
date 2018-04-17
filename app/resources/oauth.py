from tornadoalf.client import Client


class OauthConnection():
    instance = None

    def __init__(self):
        raise Exception(
            "Connection can only be instantiated through get_instance()")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Client()

        return cls.instance
