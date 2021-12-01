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
            

# 1->2->3->4-None
# after Reverse
# 4->3->2->None   1->2
# 1 is still pointing to 2 that is tail of 4 3 2
# so use it why to create a tail pointer again and again


def Reverse3(head):
    if head == None or head.next ==None:
        return head
    smallHead = Reverse3(head.next) 
    tail = head.next
    tail.next = head;
    head.next = None
    return smallHead




head = TakeInput()
Print(head)
smallHead = Reverse3(head)
Print(smallHead)