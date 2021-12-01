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


def SwapTwoNodes(head,  i, j):
    m = head
    mprev = None
    n = head
    nprev = None

    while m!=None and i > 0:
        mprev = m;
        m = m.next;
        i-=1
    while n!= None and j > 0:
        nprev = n;
        n = n.next;
        j-=1

    mprev.next = n
    nprev.next = m
    m.next = n.next
    n.next = nprev
    return head

head = TakeInput()
head1 = SwapTwoNodes(head, 1, 4)    
Print(head1)         
