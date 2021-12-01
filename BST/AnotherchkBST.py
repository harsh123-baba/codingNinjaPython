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

def Height(root):
    if(root ==None):
        return 0
    left = Height(root.left)
    right = Height(root.right)
    return 1+max(left, right);


def Search(root, key):
    if(root==None):
        return True

    if(root.data == key):
        return True
    left = False
    right = False
    if(root.data < key):
        left = Search(root.left, key)
    if root.data > key:
        right = Search(root.right, key)
    return left or right

def printBwk1k2(root, k1, k2):
    if root == None:
        return 
    if root.data > k1 and root.data < k2:
        print(root.data, end=' ')
    if root.data > k1:
        printBwk1k2(root.left, k1, k2)
    if root.data <= k2:
        printBwk1k2(root.right, k1, k2)
    

def sortedArraytoBST(A, s, e):
    if(s>e):
        return None
    mid = (s+e)//2;
    rootData = A[mid]
    root = None
    if(rootData != -1):
        root = BinaryTreeNode(rootData)
    left = sortedArraytoBST(A, s, mid-1)
    right = sortedArraytoBST(A, mid+1, e)
    root.left = left
    root.right = right
    return root

def maxTree(root):
    if(root== None):
        return -10000
    left = maxTree(root.left)
    right = maxTree(root.right)
    return max(left, right, root.data)


def minTree(root):
    if(root == None):
        return 10000
    left = minTree(root.left)
    right = minTree(root.right)
    return min(left, right, root.data)


def CheckBST(root):
    if root == None:
        return True
    leftmax = maxTree(root.left)
    rightmin = minTree(root.right)

    if(root.data <= leftmax or root.data > rightmin):
        return False
    leftBalanced = CheckBST(root.left)
    rightBalanced = CheckBST(root.right)
    return leftBalanced and rightBalanced
    
    
def CheckBSTwithMinMax(root):
    if(root==None):
        return 10000, -10000, True
    
    leftMin, leftMax, leftbal = CheckBSTwithMinMax(root.left)
    rightMin, rightMax, rightbal = CheckBSTwithMinMax(root.right)
    isBal = True
    minimum = min(rightMin, leftMin, root.data)
    maximum = max(rightMax, leftMax, root.data)


    if(root.data <= leftMax or root.data > rightMin):
        isBal= False
    if not(leftbal) or not(rightbal):
        isBal = True
    return minimum, maximum, isBal


def isBST3(root, min_val, max_val):
    if(root==None):
        return True
    if root.data < min_val or root.data >= max_val:
        return False
    isLeftconstainsok = isBST3(root.left, min_val, root.data-1)
    isrightconstainok = isBST3(root.right, root.data, max_val)

    return isLeftconstainsok and isrightconstainok

    
root = TakeInputLevel()
LevelWisePrint(root)
print(isBST3(root, -10000, 10000))


