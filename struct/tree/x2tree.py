# 二叉树的先序遍历， 中序遍历， 后序遍历
class BinTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinTree(object):
    def __init__(self):
        self._root = None

    def is_empty(self):
        # 判断二叉树是否为空
        return self._root == None

    def root(self):
        # return根节点的值
        return self._root

    def left(self):  # 返回左节点
        return self._root.left

    def right(self):  # 返回右节点
        return self._root.right

    # 先序遍历
    def pre_order(self, node):
        if node == None:
            return
        print(node.data ,end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    # 中序遍历
    def min_order(self, node):
        if node == None:
            return
        self.min_order(node.left)
        print(node.data)
        self.min_order(node.right)

    # 后序遍历
    def post_order(self, node):
        if node == None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

    # 非递归左序遍历
    def preorder(self, node):
        if not node:
            return
        stack = []
        while node or len(stack):
            if node:  # 若node存在
                print(node.data, end=' ')
                stack.append(node)  # stack保存当前node，node+1
                node = node.left  # node = node.left
            else:
                stack.pop()
                node = node.right

    # 非递归中序遍历
    def minorder(self, node):
        if not node:
            return
        stack = []
        while node or len(stack):
            if node:
                stack.append(node)
                node = node.left
            else:
                stack.pop()
                print(node.data, end=' ')
                node = node.right

    # 非递归后序遍历
    def postorder(self, node):
        if not node:
            return
        stack1 = []  #
        stack2 = []  #
        while node or len(stack1):
            if node:
                stack1.append(node)
                stack2.append(node.data)
                node = node.right
            else:
                root = stack1.pop()
                root = root.left

