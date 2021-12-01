class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None
    
    
class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def size(self):
        return self.__count


    def isEmpty(self):
        return self.size()==0;
    
    def push(self, val):
        newNode = Node(val);
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count+1
    
    
    def pop(self):
        if self.isEmpty():
            print("Hey Stack is Empty")
            return
        x = self.__head.data
        # temp = self.__head
        self.__head = self.__head.next
        self.__count = self.__count -1
        
        # del temp
        return x

    def top(self):
        if self.isEmpty():
            print("Hey ! stack is empty")
            return
        return self.__head.data

s = Stack()
s.push(10);
s.push(20)
s.push(30)

print(s.top())

while s.isEmpty() is False:
    print(s.pop(), end=" ")
print()
