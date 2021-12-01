import queue
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

def PrintDetailedTree(root):
    if root==None:
        return
    print(root.data, end=" : ")
    for child in root.children:
        print(child.data, end=", ")
    print()
    for child in root.children:
        PrintDetailedTree(child);


def TakeInput():
    print("Enter the value : ")
    rootVal = int(input())
    if rootVal == -1:
        return None
    root = Tree(rootVal)
    print("Enter the no of children of ", root.data , end=" : ")
    n = int(input())
    for i in range(n):
        child = TakeInput();
        root.children.append(child)
    
    return root;


def TakeInputLevel():
    print("Enter root Value : ")
    rootVal = int(input())
    if rootVal == -1:
        return None
    root = Tree(rootVal)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        print("Enter the number of children for ", front.data, end= " : ")
        n = int(input())
        for i in range(n):
            print("Enter the", i, " value ",front.data, end=" : ")
            childVal = int(input())
            child = Tree(childVal)
            front.children.append(child)
            q.put(child);
        
    return root

def numNodesh(root, count):
    if root == None:
        return 0;
    for child in root.children:
        count = numNodesh(child, count)

    return count+1
def numNodes(root):
    count = 0;
    return numNodesh(root, count)


def maxNodesHelper(root, max):
    if root == None:
        return max
    for child in root.children:
        if max < child.data:
            max = child.data
    return max;
def maxNodes(root):
    max = -10000
    return maxNodesHelper(root, max)


def StructurallIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    # if root1.data != root2.data:
    #     return False
    if len(root1.children)!= len(root2.children):
        return False;
    else:
        if root1.data == root2.data:
            for i in range(len(root1.children)) and  j in range(len(root2.children)):
                StructurallIdentical(root1.children[i], root2.children[j])
                return True; 


    return False



# n1 = Tree(1)
# n2 = Tree(2)
# n3 = Tree(3)
# n4 = Tree(4)
# n5 = Tree(5)
# n6 = Tree(6)
# n7 = Tree(7)

# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)
# n3.children.append(n6)
# n3.children.append(n7)
root1 = TakeInputLevel()
root2 = TakeInputLevel()
# print(numNodes(root))
# print(maxNodes(root))
print(StructurallIdentical(root1, root2))
