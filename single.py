# 单例模式

class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(Singleton, cls)
            cls._instance = origin.__new__(cls, *args, **kwargs)

        return cls._instance

class Myclass(Singleton):
    a = 1
