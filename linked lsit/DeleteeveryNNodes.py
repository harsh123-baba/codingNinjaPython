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


def DeleteNNodes(head, m,n):
    curr = head;
    prev = None;
    while curr !=None:
        i = m
        j = n
        while i>0 and curr!=None:
            prev = curr
            curr = curr.next
            i -= 1
        # temp = curr
        while j>0 and curr!= None:
            temp = curr
            prev.next = curr.next
            curr = curr.next
            del temp
            j-=1
    return head    

head = TakeInput()
head1 = DeleteNNodes(head, 2, 2)    
Print(head1)         
