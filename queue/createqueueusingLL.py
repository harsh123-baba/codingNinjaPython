class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
    

class Queue:
    def __init__(self):
        self.__head = None;
        self.__tail = None;
        self.__count = 0;

    def enqueue(self, data):
        
        newNode = Node(data)
        if(self.__head == None):
            self.__head = newNode;
            self.__tail = newNode;
            self.__count +=1;
        else:
            self.__tail.next = newNode;
            self.__tail = self.__tail.next;
            self.__count+=1;
    def dequeue(self):
        if(self.__head == None):
            return 
        temp = head;
        x = temp.data;
        self.__head = self.__head.next
        del temp;
        self.__count-=1
        return x;
    def front(self):
        if(self.__head == None):
            return        
        return self.__head.data;
    
    def size(self):
        return self.__count;

    def isEmpty(self):
        return self.size()==0

q= Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

while q.isEmpty() is False:
    print(q.dequeue())


