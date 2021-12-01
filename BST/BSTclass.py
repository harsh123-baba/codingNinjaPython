class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0;


    def printhelper(self, root):
        if(root == None):
            return
        print(root.data , end=" : ")
        if root.left!=None:
            print("L",root.left.data, end=" , ")
        if root.right!= None:
            print("R",root.right.data, end='')
        print()

        self.printhelper(root.left)
        self.printhelper(root.right);

    def PrintTree(self):
        return self.printhelper(self.root)

    
    def isPresenthelper(self, root, data):
        if root == None:
            return False
        if root.data == data:
            return True

        if root.data > data:
            return self.isPresenthelper(root.left, data)
        else:
            return self.isPresenthelper(root.right, data);
        
    
    def isPresent(self, data):
        return isPresenthelper(self.root, data)

    def InsertHelper(self, root, data):
        if root == None:
            root = BinaryTreeNode(data)
            return root
        if root.data > data:
            root.left = self.InsertHelper(root.left,data)
            return root
        
        if root.data <= data:
            root.right = self.InsertHelper(root.right, data)
            return root

    def Insert(self, data):
        self.root = self.InsertHelper(self.root, data)

    def minforDelete(self, root):
        if root == None:
            return 10000
        if root.left == None:
            return root.data
        return self.minforDelete(root.left)

    def DeleteHelper(self, root, data):
        if(root == None):
            return None
        if root.data > data :
            newLeft = self.DeleteHelper(root.left, data)
            root.left = newLeft
            return root
        if root.data < data :
            newRight = self.DeleteHelper(root.right, data)
            root.right = newRight
            return root

        else:
            if root.left == None and root.right == None:
                return None
            elif root.left==None:
                return root.right

            elif root.right == None:
                return root.left

            else:
                replacement = self.minforDelete(root.right)
                root.data = replacement
                newRightNode = self.DeleteHelper(root.right, replacement)
                root.right = newRightNode;
                return root

    
    def Delete(self, data):
        self.root=  self.DeleteHelper(self.root , data)
        return self.root;



b = BST()
b.Insert(4);
b.Insert(2);
b.Insert(6);
b.Insert(1);
b.Insert(3);
b.Insert(5);
b.Insert(7)
b.Delete(4)
b.Delete(7)
b.PrintTree()


