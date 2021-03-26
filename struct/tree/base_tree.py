class Node(object):
    '''树的节点'''
    def __init__(self, item):
        self.item = item
        self.cleft = None
        self.cright = None


class Tree(object):
    '''新增树类'''
    def __init__(self, root):
        self.root = root