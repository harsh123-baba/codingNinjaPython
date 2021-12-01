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

def MergeTwoSortedList(head1, head2):
    head = None
    tail = None
    while head1 is not None and head2 is not None:
        if(head1.data < head2.data):
            if head==None:
                head = head1;
                tail = head1
                head1= head1.next

            else:
                tail.next = head1;
                # tail = tail.next;
                tail = head1
                head1= head1.next

        else: 
            if head == None:
                head = head2
                tail = head2
                head2 = head2.next

            else:
                tail.next = head2;
                # tail = tail.next;
                tail = head2
                head2 = head2.next

    while head1 is not None:
        tail.next = head1
        tail=head1
    
    while head2 is not None:
        tail.next = head2
        tail = head2
    return head
    

head1 = TakeInput()
head2 = TakeInput()
head = MergeTwoSortedList(head1, head2)
Print(head)
