'''
BST is a data structure in which each node has at most two children, with the left child
 containing values less than the parent node and the 
right child containing values greater than the parent node, 
allowing for efficient searching and sorting operations.
'''


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#attribute of the current node object that stores the value associated with the node
    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        self.root = self._insert(self.root, key)

 #helper function and does the actual insertion
        ''' This method is recursive, 
        meaning it calls itself to traverse the tree until the appropriate location for the new node is found'''
    def _insert(self, node, key):
        if node is None:
            #creates a new TreeNode instance with the provided key
            return TreeNode(key)
        #returns True, then the new node should be placed in the left subtree
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
# work on the search functionality
    def search(self, key):
        return self._search(self.root, key)


    '''search delegates the actual search logic 
    to the private _search method that performs the actual recursive search within the binary search tree'''
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        #When the current node is None, the key to be deleted was not found hence return node
        if node is None:
            return node
        # if the target key is less than the current node key.
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left
            '''If neither one of the previous conditions is met, it means the node has both left and right children.
To choose the successor, you need to find the minimum 
value in the right subtree. The smallest value will be the in-order successor of the current node.'''

            node.key = self._min_value(node.right)
            # recursively delete the node with the minimum value from the right subtree.
            node.right = self._delete(node.right, node.key)
        return node

#finds the smallest value in a given subtree
    '''To find the smallest value in the right subtree, you need 
    to iterate through the left children of the given node until you reach the leftmost (smallest) node in the subtree.'''
    def _min_value(self, node):
        '''This condition checks if there is a 
        left child. As long as there is a left child, the loop continues and there is a smaller value to be found.'''
        while node.left is not None:
            node = node.left
        return node.key
 
 #performs an in-order traversal of the binary search tree. It returns the keys of the nodes in sorted order.
    def inorder_traversal(self):
         #store the keys of the nodes in sorted order
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        #checks if the current node (node) is not empty.
        if node:
            ##recursively call
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

#iterate over the nodes list
for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
