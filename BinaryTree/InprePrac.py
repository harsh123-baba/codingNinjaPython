import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None
        

def PrintTree(root):
    if(root == None):
        return
        

    print(root.data, end=" : ")
    if root.left:
        print(root.left.data, end=" , ")
    if root.right:
        print(root.right.data, end="")
    print()
    PrintTree(root.left)
    PrintTree(root.right)


def TakeInput():
    data = int(input())
    if(data == -1):
        return None
    root = BinaryTreeNode(data)
    left = TakeInput()
    right = TakeInput()

    root.left = left
    root.right = right
    return root

def TakeInputLevel():
    rootData = int(input())
    if(rootData == -1):
        return None        
    q = queue.Queue()
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not q.empty():
        front = q.get()
        print("Enter the left child of ", front.data, " : ")
        leftVal = int(input())
        if(leftVal != -1):
            left = BinaryTreeNode(leftVal)
            q.put(left)
            front.left = left

        print("Enter the right child of ", front.data, " : ")
        rightVal = int(input())
        if(rightVal != -1):
            right = BinaryTreeNode(rightVal)
            q.put(right)
            front.right = right


    return root
        

def PrintLevelWise(root):
    if(root==None):
        return
    # print(root.data)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        print(front.data, end=" : ")
        if(front.left):
            print(front.left.data, end=" , ")
            q.put(root.left)
        if(front.right):
            print(front.right.data, end='')
            q.put(root.right)
        print()
    
def helper(inorder, preoder, inS, inE, prS, prE):
    if(inS > inE):
        return None
    rootIndex = -1;
    for x in range(len(inorder)):
        if inorder[x]==preoder[prS]:
            rootIndex = x;
            break;
    rootData = preorder[prS]
    root = BinaryTreeNode(rootData)
    


    linS = inS;
    linE = rootIndex-1
    lprS = prS + 1
    lprE = linE - linS + lprS

    rinS = rootIndex+1
    rinE = inE
    rprS = lprE+1
    rprE = prE

    left = helper(inorder, preoder, linS, linE, lprS, lprE)
    right = helper(inorder, preoder, rinS, rinE, rprS, rprE)
    root.left=left
    root.right=right
    return root




def InPre(inorder, preorder):
    inS = 0;
    inE = len(inorder)-1
    prS = 0;
    prE = len(preorder)-1
    root = helper(inorder, preorder, inS, inE, prS, prE)
    return root



# root = BinaryTreeNode(10);
# root.left = BinaryTreeNode(20)
# root.right = BinaryTreeNode(30)

# PrintTree(root)

# root = TakeInputLevel()
# PrintLevelWise(root)
inorder = [4, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 4, 5, 3, 6, 7]
root = InPre(inorder, preorder)
# PrintLevelWise(root)
PrintTree(root)




