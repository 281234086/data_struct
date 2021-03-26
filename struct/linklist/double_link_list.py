class Node(object):
    # 节点类. 分别存放头结点和尾节点
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DoublelinkList(object):
    # 双向链表类
    def __init__(self):
        self._head = None
        self.next = None
        self.pre = None

    def is_empty(self):
        # 判断是否为空,只需判断头部是否指向none
        return self._head == None

    def length(self):
        cur = self._head
        if self.is_empty():
            return 0
        count = 1
        # while cur.next != None:
        while cur.next != None:
            cur = cur.next
            count += 1
        return count

    def ergodic(self):
        '''
        遍历所有节点
        :return:
        '''
        cur = self._head
        # while cur.next != None:
        while cur:
            print(cur.item, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        """
        头部添加
        :param item: 添加的value
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = None
        else:
            node.next = self._head
            self._head.pre = node  # 指向自身
            self._head = node


    def append(self, item):
        """
        尾部添加
        :param item:
        :return:
        """
        if self.is_empty():
            self.append(item)
        node = Node(item)
        cur = self._head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        node.pre = cur

    def insert(self, pos, item):
        """
        指定位置插入
        :param item:
        :return:
        """
        node = Node(item)
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            cur = self._head
            if count == pos:
                self.add(item)
                return
            while cur.next != None:
                pre = cur
                cur = cur.next
                count +=1
                if count == pos:
                    break

            pre.next = node
            node.pre = pre
            node.next = cur
            cur.pre = node

    # def remove(self, item):
    #     '''
    #     删除元素
    #     :param item:
    #     :return:
    #     '''
    #     if self.is_empty():
    #         raise ValueError('no item')
    #     cur = self._head
    #     if cur.item == item:
    #         self._head = cur.next
    #         if cur.next == None:# 若删除的为第一个元素,且只有一个元素
    #             pass
    #         else:  # 若删除的为第一个元素,单存在多个元素
    #             cur.next.pre = self._head
    #         return
    #     while cur:
    #         if cur.item == item:
    #             if cur.next == None:  # 若删除最后一个元素
    #                 cur.pre.next = None
    #                 return
    #             else:
    #                 cur.pre.next = cur.next
    #                 cur.next.pre = cur.pre
    #                 return
    #         else:
    #             cur = cur.next

    def remove(self, item):
        '''移除值为item的节点'''
        if self.is_empty():
            return ValueError('Null')
        cur = self._head
        if cur.next == None:
            self._head = None
        while cur.next != None:
            if cur.item == item:

                break
            else:
                cur = cur.next
        if cur.next == None:
            cur.pre = None
        else:
            if not cur.pre:
                cur.next.pre = self._head
                self._head = cur.next
            else:
                cur.pre.next = cur.next
                cur.next.pre = cur.pre

if __name__ == '__main__':
    """双向循环链表"""
    double_link = DoublelinkList()
    print(double_link.is_empty())
    double_link.add(1)
    double_link.add(2)
    print(double_link.length())
    double_link.ergodic()
    double_link.append(333)
    double_link.append(3334)
    double_link.ergodic()
    double_link.insert(2, 113)
    double_link.insert(2, 322)
    double_link.ergodic()
    print('=============')
    double_link.remove(2)
    double_link.ergodic()
    double_link.remove(322)
    double_link.ergodic()
    double_link.insert(32, 900)
    double_link.ergodic()





