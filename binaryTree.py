




# Latifa Umunyana

class BinaryTree:

 def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

 def insert(self, value):
      if value < self.value:
          if self.left is None:
              self.left = BinaryTree(value)
          else:
              self.left.insert(value)
      else:
         if self.right is None:
            self.right = BinaryTree(value)
         else:
            self.right.insert(value)

 def inorder_traversal(self):
       if self.left:
          self.left.inorder_traversal()
       print(self.value)
       if self.right:
          self.right.inorder_traversal()           

tree = BinaryTree(20)
tree.insert(5)
tree.insert(2)
tree.insert(15)
tree.insert(30)
tree.insert(3)
tree.insert(80)

tree.inorder_traversal()

