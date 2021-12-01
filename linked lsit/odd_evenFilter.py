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
    

def EvenAfterOdd(head):
    oddH = None
    oddT = None
    evenH = None
    evenT = None
    while head !=None:
        if head.data % 2 != 0:
            if oddH ==None:
                oddH = head;
                oddT = head;
                head = head.next
            else:
                oddT.next = head
                oddT = head
                head = head.next

        else:
            if evenH==None:
                evenH = head
                evenT = head
                head = head.next
            else:
                evenT.next = head
                evenT = head
                head = head.next

    oddT.next = evenH
    return oddH








head = TakeInput()
head1 = EvenAfterOdd(head)
Print(head1)


