import types

class Hello():

    impl = ""

    def process_bind_param(self, **kwargs):
        for a in kwargs:
            print(a)

a = Hello()
a.process_bind_param(hello=1)