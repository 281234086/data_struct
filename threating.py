from multiprocessing import Process, Queue
import threading
import random

q = Queue(3)
q.put(2)
q.put(23)
q.put(232)
print(q.full())

print(q.get())
print(q.get())
print(q.get())
# q.get()
# q.get()
print(q.full())