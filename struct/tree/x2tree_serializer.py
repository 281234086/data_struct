# 二叉树的序列化与反序列化

class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 序列化，将一个二叉树序列化为一个str对象
def serializer(root):
    if not root:
        return '#!'
    res = str(root.val) + '!'
    res += serializer(root.left)
    res += serializer(root.right)
    return res

# 反序列化，讲一个str对象反序列化为一个二叉树
def recoString(prestr):
    def recoserializer(values):
        key = values.pop(0)
        if key == '#':
            return None
        root = Tree(key)
        root.left = recoserializer(values)
        root.right = recoserializer(values)
        return root
    values = prestr.split('!')
    return recoserializer(values)

root = Tree(3)
root.left = Tree(2)
root.right = Tree(21)
print(root)
print(serializer(root))

a = serializer(root).split('!')
print(a)
print(a.pop(0))
print(a.pop(0))
print(a.pop(0))
print(a.pop(0))
z = recoString('3!2!#!#!21!#!#!')
print(z)
print(serializer(z))
