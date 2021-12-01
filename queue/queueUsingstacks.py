class Queue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, data):
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while len(self.__s2)!=0:
            self.__s1.append(self.__s2.pop())
        return


    def dequeue(self):
        if(self.isEmpty()):
            return -1
        return self.__s1.pop()


    def front(self):
        return self.__s1[-1];


    def size(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.size()==0

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
while  q.isEmpty() is False:
    print(q.dequeue())


