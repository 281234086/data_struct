# 单向链表

class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self._head = None
        # self._head.next = None  # 初始化一个空节点 ()

    def is_empty(self):
        # 判断当前单链表是否为空, 只需判断是否存在头节点
        if self._head == None:
            return True
        return False

    def length(self):
        cur = self._head
        if not cur:
            return 0
        else:
            n = 1
            while cur.next != None:
                cur = cur.next
                n += 1
            return n

    def ergodic(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != None:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)



    def add(self, item):
        """
        头部增加节点
        :param item: 节点值
        :return:
        """

        node = Node(item)  # 创建节点对象
        node.next = self._head  # 新增节点指向self._head指向的节点
        self._head = node  # self._head 指向新增node节点

    def append(self, item):
        """
        尾部增加节点
        :param item: 节点值
        :return:
        """
        cur = self._head
        if not cur:
            self.add(item)
        else:
            node = Node(item)
            while cur.next != None:
                cur = cur.next
            cur.next = node



    def insert(self, index, item):
        '''插入元素'''
        if index == 0:
            self.add(item)
        elif index >= self.length:
            self.append(item)
        else:
            cur = self._head
            n = 1
            node = Node(item)
            pre = None
            while cur.next != None:
                if n != index:
                    pre = cur
                    cur = cur.next
                    n += 1
                else:
                    pre.next = node
                    node.next = cur
                    break


    def remove(self, item):
        '''移除元素'''
        if self.is_empty():
            raise ValueError('null node')
        cur = self._head
        if cur.item == item:
            self._head = cur.next
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """查找元素"""
        cur = self._head
        while None != cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


MDC_DB_DICT = {
    "host": "192.168.1.243",
    "port": 3306,
    "user": "readonly",
    "password": "3XhZ9pYduyKn",
    "database": "mdc",
    "charset": "utf8",
}

{
    'db': 'mdc',
    'USER': 'readonly',
    'PASSWORD': '3XhZ9pYduyKn',
    'HOST': '192.168.1.243',
    'PORT': 3306,
}


if __name__ == '__main__':
    single = SingleLinkList()
    single.add(11)
    single.add(22)
    print(single.is_empty())
    single.ergodic()
    single.remove(2)
    single.remove(1)
    single.ergodic()
    print(single.search(22))



