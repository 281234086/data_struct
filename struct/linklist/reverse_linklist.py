# 翻转链表, 合并两个有序链表

class ListNode(object):
    # 定义链表节点类
    def __init__(self, val):
        self.value = val
        self.next = None


class Solution(object):
    def reverse_list(self, head):
        """
        翻转链表
        :param head: ListNode
        :return: ListNode
        """
        pre, cur = None, head  # cur 当前链表的节点
        while cur:
            cur.next, pre, cur = pre, cur, cur.next  # 当前链表节点的next指向pre，pre指向cur，cur指向next
        return pre

    def merge_two_list(self, list_node1: ListNode, list_node2: ListNode):
        """
        合并两个有序链表
        :param list_node1: ListNode
        :param list_node2: ListNode
        :return: ListNode
        """
        if list_node1 is None:
             return list_node2
        if list_node2 is None:
            return list_node1
        if list_node1.value < list_node2.value:
            res = list_node1
            res.next = self.merge_two_list(list_node1.next, list_node2)
        else:
            res = list_node2
            res.next = self.merge_two_list(list_node1, list_node2.next)
        return res


if __name__ == '__main__':
    listnode_1 = ListNode("hello")
    listnode_2 = ListNode("world")
    listnode_1.next = listnode_2
    print(listnode_1)
    print(listnode_1.next.value)