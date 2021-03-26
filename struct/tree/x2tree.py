class BinTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinTree(object):
    def __init__(self):
        self._root = None

    def is_empty(self):
        # 判断二叉树是否为空
        return self._root == None

    def root(self):
        # return根节点的值
        return self._root

    def lchild(self):
        return self._root.left

    def rchild(self):
        return self._root.right


