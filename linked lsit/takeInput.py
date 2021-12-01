class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def TakeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
        if currData==-1:
            break;
        newNode = Node(currData);
        if head == None:
            head = newNode
        else:
            curr= head;
            while curr.next != None:
                curr = curr.next

            curr.next = newNode;
    return head

def Display(head):
    while head!=None:
        print(head.data, end=" ")
        head = head.next
    print()
head = TakeInput();
Display(head);

