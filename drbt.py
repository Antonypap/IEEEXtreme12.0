import sys

class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

class ListBinaryTree:
    """A binary tree class with nodes as lists."""
    DATA = 0    # just some constants for readability
    LEFT = 1
    RIGHT = 2

    def __init__(self, root_value, left=None, right=None):
        """Create a binary tree with a given root value left, right the left, right subtrees"""
        self.node = [root_value, left, right]

    def create_tree(self, a_list):
        return ListBinaryTree(a_list[0], a_list[1], a_list[2])

    def insert_value_left(self, value):
        """Inserts value to the left of this node. Pushes any existing left subtree down as the left child of the new node."""
        self.node[self.LEFT] = ListBinaryTree(value, self.node[self.LEFT], None)

    def insert_value_right(self, value):
        """Inserts value to the right of this node. Pushes any existing left subtree down as the left child of the new node."""
        self.node[self.RIGHT] = ListBinaryTree(value, None, self.node[self.RIGHT])

    def insert_tree_left(self, tree):
        """Inserts new left subtree of current node"""
        self.node[self.LEFT] = tree

    def insert_tree_right(self, tree):
        """Inserts new left subtree of current node"""
        self.node[self.RIGHT] = tree

    def set_value(self, new_value):
        """Sets the value of the node."""
        self.node[self.DATA] = new_value

    def get_value(self):
        """Gets the value of the node."""
        return self.node[self.DATA]

    def get_left_subtree(self):
        """Gets the left subtree of the node."""
        return self.node[self.LEFT]

    def get_right_subtree(self):
        """Gets the right subtree of the node."""
        return self.node[self.RIGHT]

    # def __str__(self):
    #     return '['+str(self.node[self.DATA])+', '+str(self.node[self.LEFT])+', '+str(self.node[self.RIGHT])+']'

    def __str__(self):
        return str(self.node[self.DATA])

def buildtree(inorder, preorder):
    root_val = preorder[0]
    left_size = inorder.index(root_val) # size of the left subtree

    if left_size > 0:
        left = buildtree(inorder[:left_size], preorder[1:left_size+1])
    else:
        left = None

    if (left_size + 1) < len(inorder):
        right = buildtree(inorder[left_size+1:], preorder[left_size+1:])
    else:
        right = None

    return ListBinaryTree(root_val, left, right)

def traverse(root):
    current_level_left = [root]
    current_level_right = []
    # ws = ''
    # for i in range(height(root)):
    #     ws += ' '
    while (current_level_left or current_level_right):
        # sys.stdout.write(ws)
        for node in current_level_left:
            ws = ''
            h = height(node.node[node.LEFT])
            # if (node == root):
            #     h += 1
            for i in range(h):
                ws += ' '
            # if (ws == ''):
            #     ws += ' '
            # else:
            sys.stdout.write(ws)
            sys.stdout.write(str(node))
            sys.stdout.write(ws)
        sys.stdout.write(' ')
        for node in current_level_right:
            ws = ''
            h = height(node.node[node.LEFT])
            # if (node == root):
            #     h += 1
            for i in range(h):
                ws += ' '
            # if (ws == ''):
            #     ws += ' '
            # else:
            sys.stdout.write(ws)
            sys.stdout.write(str(node))
            sys.stdout.write(ws)
        # sys.stdout.write(' ')
        next_level_left = list()
        next_level_right = list()
        # ws = ws[:len(ws)//2]
        for n in current_level_left:
            # sys.stdout.write(ws)
            if n.node[n.LEFT]:
                next_level_left.append(n.node[n.LEFT])
            if n.node[n.RIGHT]:
                next_level_right.append(n.node[n.RIGHT])
        for n in current_level_right:
            # sys.stdout.write(ws)
            if n.node[n.LEFT]:
                next_level_left.append(n.node[n.LEFT])
            if n.node[n.RIGHT]:
                next_level_right.append(n.node[n.RIGHT])
        current_level_left = next_level_left
        current_level_right = next_level_right
        print()


def height(n):
    if n is None:
        return 0
    else:
        return max(height(n.node[n.LEFT]), height(n.node[n.RIGHT])) + 1

# def printLvl(root, h):
#     if (root == None):
#         return
#     q = Queue()
#     q.enqueue(root)
#     while(True):
#         nodecnt = q.size()
#         if (nodecnt == 0):
#             break
#         for i in range(h):
#             sys.stdout.write('  ')
#         while(nodecnt > 0):
#             node = q.dequeue()
#             sys.stdout.write(node.node[node.DATA])
#
#             if(node.node[node.LEFT] != None):
#                 q.enqueue(node.node[node.LEFT])
#             if(node.node[node.RIGHT] != None):
#                 q.enqueue(node.node[node.RIGHT])
#
#             if(nodecnt>1):
#                 sys.stdout.write('  ')
#             nodecnt -= 1
#         h -= 1
#         print()


#main

isInfix = True
infix, prefix = "", ""
for line in sys.stdin:
    if isInfix:
        infix = line.strip()
        isInfix = False
        continue
    else:
        prefix = line.strip()
        isInfix = True

    inorder_seq = infix
    preorder_seq = prefix
    root = preorder_seq[0]

    tree = ListBinaryTree(root)

    binary = buildtree(inorder_seq, preorder_seq)

    traverse(binary)
    # printLvl(binary, height(binary))
    # print(binary)
    # print(height(binary))
    # print(binary.DATA)
