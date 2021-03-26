# 向有环链表中插入新节点

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


def insertNum(head, item):
    node = Node(item)
    if head == None:
        head.next = node
        return node

    node = head
    pre = node
    cur = node.next
    while cur != head:
        if pre.value > item and cur.value < item:
            break
        pre = pre.next
        cur = cur.next
    pre.next = node
    node.next = cur
    return head


