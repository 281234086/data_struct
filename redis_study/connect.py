from redis import Redis

client = Redis()
print(client.ping())
if client.ping():
    print(1111111111)


a = [2,3,4, 123,333, 1]
b = (1,2,3,4,5)
print(zip(a, b))
a = list(zip(a, b))
print(a)

a = '2020-01-01 02:02:00'
import datetime
a = datetime.datetime.strptime(a, '%Y-%m-%d %X')
print(a)
b = a + datetime.timedelta(hours=8)
print(b)


