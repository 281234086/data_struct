# 单向循环列表

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycleLink(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0
        n = 1
        cur = self._head  # 头节点
        while cur.next != self._head: # 若
            cur = cur.next
            n += 1
        return n

    def ergodic(self):
        '''
        遍历所有节点
        :return:
        '''
        if self.is_empty():
            raise ValueError('null error')

        cur = self._head
        while cur.next != self._head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def add(self, item):
        """
        头部添加
        :param item: 添加的value
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = self._head
            # cur.next = node

    def append(self, item):
        """
        尾部添加
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            node.next = node
            self._head = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''
        指定位置插入
        :param pos: 指定位置
        :param item: value
        :return:
        '''
        node = Node(item)
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)

        else:
            cur = self._head
            pre = None
            count = 0
            while cur.next != self._head:
                if count != pos:
                    count += 1
                    pre = cur
                    cur = cur.next
                else:
                    break
            node.next = cur
            pre.next = node

    def remove(self, item):
        """
        删除值为item的节点
        :param item:
        :return:
        """
        if self.is_empty():
            raise ValueError('当前值不存在')
        cur = self._head
        pre = None
        if cur.item == item:
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
        else:
            pre = self._head
            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:  # 若item在最后一个节点
                pre.next = cur.next





if __name__ == '__main__':
    """单向循环链表"""
    sc = SingleCycleLink()
    sc.add(11)
    sc.add(1212)
    sc.ergodic()
    sc.add('23333333333')
    print('ajsdlkfjl')
    sc.ergodic()
    sc.add(33333)
    sc.append(2)
    sc.ergodic()
    sc.insert(2,'qiao')
    sc.ergodic()
    sc.remove('qiao')
    sc.ergodic()






















