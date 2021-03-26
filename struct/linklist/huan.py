# 判断一个链表是否有环

class Node(object):
    def __init__(self):
        self.head = None
        self.next = None

def get_first_meet(head):
    fast = head.next
    slow = head.next.next
    while fast != slow:
        if fast != None or slow != None:
            return None
        fast = fast.next.next
        slow = slow.next

    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast