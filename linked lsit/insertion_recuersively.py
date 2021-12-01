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


def Insert(head, i, x):
    newNode = Node(x);
    curr = head
    prev = curr

    if i == 1:
        newNode.next = head;
        head = newNode
        return
    while i>1:
        prev = curr
        curr = curr.next
        i-=1
    prev.next = newNode;
    newNode.next = curr


def InsertRecursive(head, i, x):
    if i <= 0:
        return None
    if head == None:
        return None

    if i ==1:
        newNode = Node(x)
        newNode.next = head
        return newNode
    smallHead = InsertRecursive(head.next, i-1, x)
    head.next = smallHead
    return head

def DeleteRecursive(head, i):
    if i==1:
        curr = head;
        head = head.next
        del curr
        return head
    smallHead = DeleteRecursive(head.next, i-1)
    head.next = smallHead
    return head



def Delete(head, i):
    curr = head
    prev = curr
    if i==1:
        curr = head
        head = head.next
        x = curr.data
        del curr
        return x
    
    while i>1:
        prev = curr;
        curr = curr.next
        i-=1
    prev.next = curr.next
    x = curr.data
    del curr
    return x;
        


        
    


head = TakeInput()
InsertRecursive(head, 2, 100)
Print(head) 

print(DeleteRecursive(head, 1))
Print(head) 

print(ithElement(head, 4))
