class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def TakeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = head
    for currData in inputList:
        if currData == -1:
            break;
        newNode = Node(currData);
        if head == None:
            head = newNode
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

def lengthLL(head):
    count = 0;
    while head != None:
        count+=1
        head = head.next
    return count

def ithElement(head, i):
    if i > lengthLL(head):
        return -1
    while i >1:
        head = head.next
        i-=1
    return head.data


head = TakeInput()
Print(head) 
print(ithElement(head, 4))
