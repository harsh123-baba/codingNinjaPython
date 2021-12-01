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
    

def helper(head, n, i):
    if head.data == n:
        return i;
    
    return helper(head.next, n, i+1)




def FindNode(head, n):
    i = 0;
    return helper(head, n, i);


head1 = TakeInput()


Print(head1)
print(FindNode(head1, 2))


