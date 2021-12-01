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



def IsBalanced(root):
    if(root == None):
        return True
    left = Height(root.left);
    right = Height(root.right);
    
    if left -right >1 or right - left>1:
        return False

    leftBal = IsBalanced(root.left)
    rightBal = IsBalanced(root.right) 
    if(leftBal and rightBal):
        return True
    return False

def getheightAndIsBalanced(root):
    if(root == None):
        return 0, True
    lh, lBal = getheightAndIsBalanced(root.left)
    rh, rBal = getheightAndIsBalanced(root.right)
    h = 1+max(lh, rh);
    if(lh -rh >1 or rh-lh>1):
        return h, False
    if lBal and rBal :
        return h, True

    else:
        return h, False



class IsBal:
    def __init__(self):
        self.h = 0;
        self.bal = True
    
def getBal(root):
    if(root==None):
        s = IsBal()
        s.h = 0;
        bal = True
        return s

    leftS = IsBal()
    rightS = IsBal()
    leftBal = IsBal()
    rightBal = IsBal()
    s = IsBal()
    leftS = getBal(root.left)
    rightS = getBal(root.right)
    

    # leftS.h = lh;
    # rightS.h = rh;
    # leftS.bal = 

    h = 1+ max(leftS.h, rightS.h);
    if(leftS.h - rightS.h > 1 or rightS.h - leftS.h > 1):
        s.h = h
        s.bal = False
        return s
    if leftS.bal and rightS.bal:
        s.h = h;
        s.bal = True
        return s
    else:
        s.h = h;
        s.bal = False
        return s;
        

def Diameter(root):
    if(root==None):
        return 0;
    left = Diameter(root.left)
    right = Diameter(root.right)
    return 1+left+right


def InPrehealper(i, p, ps, pe, ist, ie):
    if(ist > ie):
        return None
    rootIndex = -1;
    for x in range(len(i)):
        if(i[x]==p[ps]):
            rootIndex = x
            break;
    rootData = p[ps];
    root = BinaryTreeNode(rootData);
    linS = ist
    linE = rootIndex-1
    lpS = ps+1
    lpE = linE-linS +lpS

    rinS = rootIndex+1;
    rinE = ie
    rpS = lpE+1
    rpE = pe

    left = InPrehealper(i, p, lpS, lpE, linS, linE);
    right = InPrehealper(i, p, rpS, rpE, rinS, rinE);
    root.left = left
    root.right = right
    return root


def InPre(i, p):
    ps = 0;
    pe = len(p)-1;
    ist = 0;
    ie = len(i)-1;

    root = InPrehealper(i, p, ps, pe, ist, ie);
    return root



# root = TakeInputLevel()
# Inorder(root);
# Preorder(root);
# print()
# print(IsBalanced(root))
# s = IsBal()

# s = getBal(root)
# print(s.bal)
# print(getheightAndIsBalanced(root))

# print(Diameter(root))
# print(sumOfNodes(root))

# inorder = [2, 1, 3]
# pre = [1, 2, 3];
inorder = [4, 2, 5, 1, 6, 3, 7]
pre = [1, 2, 4, 5, 3, 6, 7]
root = InPre(inorder, pre)
PrintBinartTree(root)

 
