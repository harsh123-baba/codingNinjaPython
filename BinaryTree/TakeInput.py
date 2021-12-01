class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintBinartTree(root):
    if(root== None):
        return
    print(root.data, end=" : ")
    if root.left != None:
        print(root.left.data, end=" , ")
    if root.right !=None:
        print(root.right.data, end='')
    print()
    PrintBinartTree(root.left)
    PrintBinartTree(root.right)


def TakeInput():
    rootData = int(input())
    if(rootData == -1):
        return None
    root = BinaryTreeNode(rootData)
    leftTree = TakeInput()
    rightTree = TakeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = TakeInput()
PrintBinartTree(root)
