# Node
# -----------------------------------------------------------------------------

class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
		self.prev = None


# Single Linked List
# -----------------------------------------------------------------------------

# __init__: initializes empty list
# __repr__: string representation of keys of list
# Boolean IsEmpty(): is the list empty 
# SetHead(key): add item as head of linked list
# Boolean Find(key): find key in list
# Erase(key): remove a key from the list
# AddBefore(Node, key): add key before node
# AddAfter(Node, key): add key after node	
# PushFront(key): add item to front
# PopFront(): remove and return front item
# PushBack(key): add item to back
# PopBack(): remove and return back item

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __repr__(self):
		"""
		represent the list as an string of its keys.
		"""
		val = ""
		n = self.head
		while n is not None:
			if n == self.tail:
				val += str(n.key)
				return val
			val += (str(n.key) + " ")
			n = n.next
		return val


	def isEmpty(self):
		return self.head is None

	def SetHead(self, key=None):
		if self.head is None:
			self.head = Node(key)
			self.tail = self.head
			self.size += 1
		return

	def Find(self,key):
		"""
		Boolean: is this key in the linked list
		"""
		if self.head is None:
			return "ERROR: empty list"
		else:
			n = self.head
			while n is not None:
				if n.key == key:
					return True
				else:
					n = n.next
			return False


	def Erase(self,key):
		"""
		Erases key from linked list
		"""
		if self.isEmpty():
			return "ERROR: Empty List"
		n = self.head
		if n.key == key:
			self.PopFront()
			return
		while n.next is not None:
			if n.next.key == key:
				n.next = n.next.next
				self.size -= 1
				return
			else:
				n = n.next
		return "Key not found"

	def AddBefore(self,node,key):
		"""
		Add new item before item in list.
		"""
		if self.isEmpty():
			return "Empty List."	
		n = self.head
		if n.key == node:
			lst.PushFront(key)
			return
		else:
			n = n.next
			while n.next is not None:
				if n.next.key == node:
					new_node = Node(key)
					new_node.next = n.next
					n.next = new_node
					lst.size += 1
					return
				else:
					n = n.next
			return "Key not found"

	def AddAfter(self,node,key):
		"""
		Add new item before item in list.
		"""
		if self.isEmpty():
			return "Empty List."	
		n = self.head
		while n is not None:
			if n.key == node:
				new_node = Node(key)
				new_node.next = n.next
				n.next = new_node
				lst.size += 1
				return
			else:
				n = n.next
		return "Key not found"
				
			

	def PushFront(self, key):
		"""
		Add item to front of list.
		"""
		if self.head is None:
			self.SetHead(key)
		else:
			new_node = Node(key)
			new_node.next = self.head
			self.head = new_node
			self.size += 1


	def PopFront(self):
		"""
		Remove front item and return its key.
		"""
		if self.head is None:
			return "ERROR: empty list."
		else:
			ret_val = self.head
			self.head = self.head.next
			self.size -= 1
			return ret_val.key

	def PushBack(self, key):
		"""
		Adds item to the back of the list.
		"""
		new_node = Node(key)
		new_node.next = None
		if self.tail is None:
			self.SetHead(key)
		else:
			self.tail.next = new_node
			self.tail = new_node
			self.size += 1

	def PopBack(self):
		"""
		Removes and returns list item from the back.
		"""
		if self.head is None:
			return ("ERROR: empty list")
		elif self.head == self.tail:
			p = self.head
			self.head = None
			self.tail = None
			self.size -= 1
			return p.key
		else:
			p = self.head
			while p.next.next is not None:
				p = p.next
			ret_val = p.next			
			p.next = None
			self.tail = p
			self.size -= 1
			return ret_val.key
