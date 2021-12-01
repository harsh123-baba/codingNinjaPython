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

def MidOfLL(head):
    slow = head
    fast = head

    while fast.next!=None and fast.next.next != None:
        slow = slow.next
        fast = fast.next
        if fast!=None:
            fast = fast.next

    return slow

def Merge(head):
    mid = MidOfLL(head)
    right = mid.next
    mid.next = None
    left = head;

    if head is None:
        return head
    finalHead = None
    finalTail = None;
    while left is not None and right is not None:
        if left.data < right.data:
            if finalHead == None:
                finalHead = left
                finalTail = finalHead

            else:
                finalTail.next = left
                finalTail = finalTail.next
            left = left.next
        else:
            if finalHead == None:
                finalHead = right
                finalTail = finalHead
            else:
                finalTail.next = right
                finalTail = finalTail.next
            right = right.next

    return finalHead





head = TakeInput()
# head2 = TakeInput()
head1 = Merge(head) 
Print(head1)