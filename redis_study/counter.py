# class Counter():
#
#     def __init__(self, client, key):
#         self.client = client
#         self.key = key
#
#     def increase(self, n=1):
#         return self.client.incr(self.key, n)
#
#     def decrease(self, n=1):
#         return self.client.decr(self.key, n)
#
#
#
# from redis import Redis
#
# client = Redis()
# for i in range(10):
#     client.hincrby('hello', 'qiao_%s' % i, 1)
# print(client.hgetall('art:111'))

