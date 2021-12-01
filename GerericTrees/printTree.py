class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

def PrintTree(root):
    if root==None:
        return
    print(root.data)
    for child in root.children:
        PrintTree(child)

n1 = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)
n7 = Tree(7)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)
n3.children.append(n6)
n3.children.append(n7)

PrintTree(n1)



