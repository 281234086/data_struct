# 二叉树的按层打印

class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def x2print(root):
    if not root:
        return

    que_list = [] # 用来存放节点
    # que_list.append(last)
    que_list.append(root)
    while que_list:
        root = que_list.pop(0)
        print(root.val, end=' ')
        if root.left:
            que_list.append(root.left)
        if root.right:
            que_list.append(root.right)


a = Tree(2)
a.left = Tree(3)
a.left.left = Tree(44)
a.left.right = Tree(33)
a.right = Tree(4)
x2print(a)

