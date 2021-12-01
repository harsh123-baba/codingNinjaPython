class Stack:

    def __init__(self):
        self.__data = []

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size()==0;

    def top(self):
        if self.isEmpty():
            print("Hey ! stack is empty already")
            return
        return self.__data[len(self.__data)-1]
    
    
    def push(self, val):
        self.__data.append(val)
    
    
    def pop(self):
        if self.isEmpty():
            print("Hey ! stack is empty already")
            return
        return self.__data.pop()
    
    

s= Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.top())
# print()
while s.isEmpty() is False:
    print(s.pop(), end=' ')


print()
print(s.top())