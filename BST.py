#Create Node
class Node:
    #create constructor
    def __init__(self, value):
        #data value
        self.value = value
        #left and right child nodes
        self.leftChild = None
        self.rightChild = None

    #insert data
    def insert(self, data):
    """
    param: data - value 
    return: boolean
    """
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            self.rightChild = Node(data)
            return True

    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    # recursive traversals
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


    def postorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

#user interface
class Tree:
    #constructor
    def __init__(self):
        #root node for tree
        self.root = None

    #accepts piece of data to insert
    def insert(self, data):
        #check if root node exists, if yes add
        if self.root:
            #recursive addition
            return self.root.insert(data)
        #if root node does not exist, create new node
        else:
            self.root = Node(data)


#Find value function
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder")
        self.root.preorder()

    def postorder(self):
        print("postorder")
        self.root.postorder()

    def inorder(self):
        print("inorder")
        self.root.inorder()
        

bst = Tree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.preorder()
bst.postorder()
bst.inorder()
