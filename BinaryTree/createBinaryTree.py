class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    


def PrintBinaryTree(root):
    if(root == None):
        return
    print(root.data, end=" : ")
    if root.left != None:
        print("L",root.left.data, end=",")
    if root.right!=None:
        print("R", root.right.data, end='')
    print()
    PrintBinaryTree(root.left)
    PrintBinaryTree(root.right)


root = BinaryTreeNode(10)
lchild = BinaryTreeNode(20)
rchild = BinaryTreeNode(30)
llchild = BinaryTreeNode(40)
rlchild = BinaryTreeNode(50)


root.left = lchild
root.right = rlchild
lchild.left = llchild
lchild.right = rlchild

PrintBinaryTree(root)

