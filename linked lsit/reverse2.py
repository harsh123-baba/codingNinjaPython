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
        print(head.data, end="->")
        head = head.next
    print("None")


# def Reverse(head):
#     if head.next == None  or head is None:
#         return head;

#     smallHead = Reverse(head.next)
#     tail = smallHead;
#     while tail.next!=None:
#         tail = tail.next
#     tail.next = head
#     head.next = None;
#     return smallHead
            

def Reverse1(head):
    if head ==None or head.next==None:
        return head

    smallHead = Reverse1(head.next)
    tail = smallHead
    while tail.next != None:
        tail = tail.next

    tail.next = head
    head.next = None
    return smallHead

def Reverse2(head):
    if head == None or head.next == None:
        return head, head
    
    smallHead,smallTail = Reverse2(head.next)
    smallTail.next = head
    head.next = None
    return smallHead, head;


head = TakeInput()
Print(head)
# smallHead = Reverse1(head)   
# Print(smallHead)
smallHead2, tail = Reverse2(head)
Print(smallHead2)