class Node:
    def __init__(self, data):
        self.data = data
        self.next = None;


def TakeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        
        newNode = Node(currData);
        if head == None:
            head = newNode;
            tail = head
        else:
            tail.next = newNode
            tail = newNode
    return head;

def Print(head):
    while head != None:
        print(head.data, end=" ")
        head = head.next
    print()


head = TakeInput()
Print(head)     