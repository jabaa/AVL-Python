__author__ = 'Thomas Sablik'

from AVL import AVL

avl = AVL()
avl.insert(67)
avl.insert(58)
avl.insert(19)
avl.insert(24)
avl.insert(57)
avl.insert(78)
avl.insert(74)
avl.insert(72)
avl.insert(82)
avl.insert(87)

print("avl:")
print(avl)

print("avl.max: " + str(avl.get_max()))
