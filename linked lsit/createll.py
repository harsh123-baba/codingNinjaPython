class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


def Print(head):
    while head!=None:
        print(head.data, end=' ')
        head = head.next
    print()
n1 = Node(2);
n2 = Node(12);
n1.next = n2

print(n2.data)
print(n1.data)
print(n1.next.data)
Print(n1)
# print()
