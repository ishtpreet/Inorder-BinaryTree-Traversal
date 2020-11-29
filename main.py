class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)


def InOrder(root):
    # code he
    listt = []
    listt = helperFunc(root, listt)
    return listt
    
    
def helperFunc(root, listt):
    if root:
        helperFunc(root.left, listt)
        listt.append(root.value)
        helperFunc(root.right, listt)
    return listt

#Setting Up BinaryTree
'''
         5
       /   \
      4     6
    /   \     \
   3     2     8
'''
tree = BinaryTree(5)
tree.root.left = Node(4)
tree.root.right = Node(6)
tree.root.left.left = Node(3)
tree.root.left.right = Node(2)
tree.root.right.right = Node(8)

traversal = InOrder(tree.root)
print(traversal)