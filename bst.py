# =============================================================================
# file:    bst.py
# title:   Binary Search Trees in Python
# author:  Nura Kawa
# date:    02.03.2019
# =============================================================================


# Node 
# -----------------------------------------------------------------------------
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

	def list_of_children(self): # for BST definition
		children = ()
		if self.left is not None:
			children += (self.left,)
		if self.right is not None:
			children += (self.right)
		return children


# Queue
# -----------------------------------------------------------------------------
# This is implemented for use in function LevelTraversal. 
# I use Node as defined above, where its "right" is its "next" pointer.
 
class Queue:

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def is_empty(self):
		return self.head is None

	def add_head(self, head):
		self.head = Node(head)
		self.tail = self.head
		self.size += 1

	def enqueue(self, key):
		if self.head is None:
			return self.add_head(key)
		else:
			new_tail = Node(key)			
			self.tail.right = new_tail
			self.tail = new_tail
			self.size += 1

	def dequeue(self):
		if self.head is None:
			self.tail = None
			return
		else:
			ret_val = self.head.key
			new_head = self.head.right
			self.head = new_head
			self.size -= 1
			return(ret_val)



# Binary Search Tree
# -----------------------------------------------------------------------------
# based on: https://gist.github.com/jakemmarsh/8273963

# definition: a tree is either empty or a node with 
# (1) a key and value (2) a list of child trees.

class BST(Node):

	def __init__(self):
		self.root = None

	def insert(self, key):
		if self.root is None:
			self.root = Node(key)
		else:
			self.add_node(self.root, key)

	def add_node(self, current_node, key):
		if key <= current_node.key:
			if current_node.left is not None:
				self.add_node(current_node.left, key)
			else:
				current_node.left = Node(key)
		else:
			if current_node.right is not None:
				self.add_node(current_node.right, key)
			else:
				current_node.right = Node(key)

	def find(self, val):
		return self.find_node(self.root, key)

	def find_node(self, current_node, key):
		if current_node is None:
			return False
		elif key == current_node.key:
			return True
		elif key <= current_node.key:
			return find_node(current_node.left, key)
		elif key > current_node.key:
			return find_node(current_node.right, key)

	def height(self):
		return self.find_height(self.root)

	def find_height(self, current_node):
		if current_node is None:
			return 0
		return (1 + max( self.find_height(current_node.left), self.find_height(current_node.right) ))

	def size(self):
		return self.find_size(self.root)

	def find_size(self, current_node):
		if current_node is None:
			return 0
		return (1 + self.find_size(current_node.left) + self.find_size(current_node.right))

	# Depth-first search

	def InOrderTraversal(self):
		return self.helper_InOrder(self.root)
	
	def helper_InOrder(self, current_node):
		if current_node is None:
			return
		else:
			self.helper_InOrder(current_node.left)
			print(current_node.key)
			self.helper_InOrder(current_node.right)

	def PreOrderTraversal(self):
		return self.helper_PreOrder(self.root)

	def helper_PreOrder(self, current_node):
		if current_node is None:
			return
		else:
			print(current_node.key)
			if current_node.left is not None:
				self.helper_PreOrder(current_node.left)
			if current_node.right is not None:
				self.helper_PreOrder(current_node.right)


	def PostOrderTraversal(self):
		return self.helper_PostOrder(self.root)

	def helper_PostOrder(self, current_node):
		if current_node is None:
			return
		else:
			if current_node.left is not None:
				self.helper_PostOrder(current_node.left)
			if current_node.right is not None:
				self.helper_PostOrder(current_node.right)
			print(current_node.key)
			
	# Breadth-first search
	
	def LevelTraversal(self):
		return self.helper_LevelTraversal(self.root)


	def helper_LevelTraversal(self, current_node, q = Queue()):
		if current_node.key is None:
			return
		else:
			q.enqueue(current_node)
		while q.is_empty() == False:
			node = q.dequeue()
			print(node.key)
			if node.left is not None:
				q.enqueue(node.left)
			if node.right is not None:
				q.enqueue(node.right)
