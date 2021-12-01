class Queue:
    def __init__(self):
        self.__arr = []
        self.__count = 0;
        self.__front = 0;

    def enqueue(self, data):
        self.__arr.append(data)
        self.__count +=1
    
    def dequeue(self):
        if self.size()==0:
            return 
        element = self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return element

    def front(self):
        return self.__arr[self.__front];

    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size()==0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.front())
print()
while q.isEmpty() is False:
    print(q.dequeue())
