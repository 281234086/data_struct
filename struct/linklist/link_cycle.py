# class ChangeLink(object):
#
#     def __init__(self):
#         self._head = None
#         self.next = None
#
#     def action(self, node):
#         one_cur = self._head
#         # two_cur = self._head
#         while one_cur.next != None:
#             one_cur = one_cur.next  # 走一步
#             two_cur = one_cur.next  # 走两步
#
#         two_cur = one_cur.next
#         one_cur.next = None
#         while two_cur != None:
#

class A(object):
    def __init__(self, hello):
        self.__hello = 32

    def hello(self):
        return self.__hello

class B(object):
    __hello = '123'

    @property
    def hello(self):
        return self.__hello

a = A(22)
print(a.hello())

