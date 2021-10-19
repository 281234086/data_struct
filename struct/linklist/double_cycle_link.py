# 双向循环链表

class Node(object):
    '''定义链表对象'''
    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


class DoubleCycleLink(object):
    """双向循环链表"""
    def __init__(self, item):
        self._head = None
        self.pre = None
        self.next = None

    def is_empty(self):
        # 判断是否为空,只需判断头部是否指向self._head
        return not self._head

    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count


    def ergodic(self):
        '''
        遍历所有节点
        :return:
        '''
        if self.is_empty():
            raise ValueError('Null!')
        cur = self._head.next
        print(self._head.item, end=' ')
        while cur != self._head:
            print(cur.item, end = ' ' )
            cur = cur.next
        print()


    def add(self, item):
        """
        头部添加
        :param item: 添加的value
        :return:
        """
        node = Node(item)
        if self.is_empty(): # 若为空
            self._head = node
            node.next = self._head
            node.pre = node
        else:
            node.next = self._head  # 新增节点的next指向self._head指向的Node
            node.pre = self._head.pre  # 新增节点的pre指向self._head前的节点
            self._head.pre.next = node  # 尾节点的next指向node
            self._head.pre = node  # 原首节点的pre指向node
            self._head = node  # 移动self._head 指向node


    def append(self, item):
        """
        尾部添加
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
            node.pre = node
            return
        cur = self._head
        while cur.next != self._head:
            cur = cur.next

        cur.next = node
        node.pre = cur
        node.next = self._head
        self._head.pre = node


    # def insert(self, pos, item):
    #     """
    #     指定位置插入
    #     :param item:
    #     :return:
    #     """
    #     if pos <= 0:
    #         self.add(item)
    #     elif pos >= self.length()-1:
    #         self.append(item)
    #     else:
    #         count = 1
    #         cur = self._head.next
    #         node = Node(item)
    #         while cur.next != self._head:
    #             if pos == count:
    #                 node.next = cur
    #                 node.pre = cur.pre
    #                 cur.pre.next = node
    #                 cur.pre = node
    #                 return
    #             else:
    #                 count += 1
    #                 cur = cur.next

    def insert(self, pos, item):
        '''
        在pos点插入item
        :param pos: 插入位置
        :param item: 插入value
        :return:
        '''
        node = Node(item)
        if pos <= 0:  # 若插入位置小于0, 则在首节点插入
            self._head = node
            node.next = node
        elif pos > (self.length() - 1):  # 若插入位置大于链表长度.尾部插入
            self.append(item)
        else:
            cur = self._head
            count = 0
            while cur.next != self._head:
                if pos == count: #若插入位置等于节点所在位置
                    node.next = cur # 新增节点node的next指向当前节点
                    cur.pre.next = node # 当前节点前节点的next指向node
                    cur.pre = node # 当前节点的pre指向新增节点node
                    node.pre = cur.pre # 新增节点node的pre指向前cur的pre
                    return
                else:
                    cur = cur.next
                    count += 1
            if count == pos: # 若为尾节点
                cur.pre.next = node
                node.pre = cur.pre
                node.next = cur
                cur.pre = node


    def remove(self, item):
        '''
        删除元素
        :param item:
        :return:
        '''
        if self.is_empty():
            raise ValueError('Null')
        cur = self._head
        if cur.item == item:
            self._head = None
        while cur.next != self._head:
            if cur.item == item:
                if cur.next == self._head:  # 若为最后一个节点
                    cur.pre.next = self._head
                    self._head.pre = cur.pre
                else:
                    cur.pre.next = cur.next # 若不为最后一个节点
                    cur.next = cur.pre
                return
            else:
                cur = cur.next




if __name__ == '__main__':
    double_cycle = DoubleCycleLink(233)
    print(double_cycle.is_empty())
    print(double_cycle.length())
    double_cycle.add(123)
    double_cycle.ergodic()
    double_cycle.append(233)
    double_cycle.ergodic()
    double_cycle.append(2331)
    double_cycle.ergodic()
    print('============')
    double_cycle.insert(2, 321321321)
    double_cycle.ergodic()

    double_cycle.insert(1, 1)
    double_cycle.ergodic()

    double_cycle.insert(2, 33333333)
    print('------------')
    double_cycle.ergodic()
    double_cycle.remove(233)
    double_cycle.ergodic()

