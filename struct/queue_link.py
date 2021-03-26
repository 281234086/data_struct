class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, item):
        '''栈新增数据'''
        self.item.append(item)

    def size(self):
        '''判断栈的长度'''
        return len(self.item)
    def is_empty(self):
        '''判断是否为空'''
        return not self.item

    def pop(self):
        '''删除栈尾元素'''
        self.item.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.item[:-1]


