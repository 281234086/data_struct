# 判断一个链表是否为回文结构

def huiwen(arr):
    if arr == None or len(arr) < 2:
        return True
    stack = []
    cur = arr
    while cur != None:
        stack.append(cur.item)
        cur = cur.next
    while stack:
        if stack.pop().item != arr.item:
            return False
        arr = arr.next
    return True
