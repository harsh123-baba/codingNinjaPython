import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None


def PrintBinartTree(root):
    if(root==None):
        return
    print(root.data, end=" : ")
    if root.left != None:
        print("L",root.left.data, end=" , ")

    if root.right != None:
        print("R", root.right.data, end='')
    print()
    PrintBinartTree(root.left)
    PrintBinartTree(root.right)




def TakeInputLevel():
    rootData = int(input())
    q = queue.Queue()
    root=None;
    if rootData!= -1:
        root = BinaryTreeNode(rootData)
        q.put(root)

    while  not q.empty():
        front = q.get();
        # q.get()
        print("Enter the ", front.data, "left child value")
        leftVal = int(input())
        if leftVal != -1:
            left = BinaryTreeNode(leftVal);
            q.put(left)
            front.left = left
        print("Enter the ", front.data, "right child value ")
        rightVal = int(input())
        if rightVal != -1:
            right =BinaryTreeNode(rightVal);
            q.put(right)
            front.right = right
    return root

def LevelWisePrint(root):
    if root==None:
        return;
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        print(front.data, end=" : ")
        if front.left:
            print("L",front.left.data, end=" , ")
            q.put(front.left)

        if front.right:
            print("R",front.right.data, end='')
            q.put(front.right)
        print()

def numNodes(root):
    if(root == None):
        return 0
    left = numNodes(root.left)
    right = numNodes(root.right)
    return 1+left+right

# 1 2 3 4 5 -1 -1 -1 -1 -1 -1

def sumOfNodes(root):
    if(root==None):
        return 0;
    left = sumOfNodes(root.left)
    right = sumOfNodes(root.right)
    return root.data + left + right

def Preorder(root):
    if(root == None):
        return
    print(root.data, end=" ")
    left = Preorder(root.left)
    right = Preorder(root.right)

def Inorder(root):
    if root== None:
        return
    
    left = Inorder(root.left)
    print(root.data, end=" ")
    right = Inorder(root.right)


def RemoveLeafNodes(root):
    if(root == None):
        return None
    if(root.left == None and root.right == None):
        return None
    
    root.left = RemoveLeafNodes(root.left)
    root.right = RemoveLeafNodes(root.right)
    return root



root = TakeInputLevel()
# Inorder(root)
PrintBinartTree(root)
root1 = RemoveLeafNodes(root)
print()
# print(sumOfNodes(root))
PrintBinartTree(root)