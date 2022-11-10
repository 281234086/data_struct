# class A():
#     def __init__(self):
#         self.x = 0
#
# class B(A):
#     def __init__(self):
#         self.y = 1
#
# b = B()
# print(b.x, b.y
#       )

a = [1, 2, 'charles']
print(a[-1][-2])
def foo(k):
    k[0] = 1
q = [0]
foo(q)
print(q)

import re

matchobj = re.compile(r'''(?i)^[^?#]+\?([^#]+)''')
subject = 'http://www.regexcookbook.com?param=value'
match = matchobj.search(subject)
if match:
    print(match.group(1))
