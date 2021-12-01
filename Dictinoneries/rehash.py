class MapNode:
    def __init__(self, key, value):
        self.key = key;
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 3
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0;
    
    def size(self):
        return self.count
    
    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketSize))

    def rehash(self):
        temp = self.bucket
        self.bucket = [None for i in range(2*self.bucketSize)]
        oldSize = self.bucketSize;
        self.bucketSize = self.bucketSize*2;
        self.count =0;
        for i in range(oldSize):
            head = self.bucket[i];
            while head!=None:
                key = head.key
                value = head.value
                self.Insert(key, value)
                head = head.next

        for i in range(oldSize):
            head = temp[i]
            del head;
        del temp;



    def Insert(self, key, value):
        hc = hash(key)
        bucketIndex = self.getBucketIndex(hc)
        head = self.bucket[bucketIndex]
        while head!=None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        loadFactor= self.count/self.bucketSize;
        if loadFactor<0.7:
            head = self.bucket[bucketIndex]
            newnode = MapNode(key, value)
            newnode.next = head
            self.bucket[bucketIndex] = newnode
            self.count+=1
        else:
            self.rehash();
    
    def remove(self, key):
        hc = hash(key)
        bucketIndex = self.getBucketIndex(hc)
        head = self.bucket[bucketIndex]
        prev = None;
        while head != None:
            if head.key == key:
                if prev == None:
                    self.bucket[bucketIndex]= head.next
                else:
                    prev.next = head.next

                value = head.value
                del head;
                self.count-=1;
                return value
            prev = head
            head = head.next



    def search(self, key):
        hc = hash(key)
        bucketIndex = self.getBucketIndex(hc)
        head = self.bucket[bucketIndex]
        while head != None:
            if head.key == key:
                return True
            head = head.next
        return False



m = Map()
m.Insert("harsit", 20)
m.Insert("harsi", 20)
m.Insert("harst", 20)
m.Insert("harit", 20)
# m.Insert("hasit", 20)
# m.Insert("hrsit", 20)
# m.Insert("arsit", 20)
# m.Insert("harsit1", 20)
# m.Insert("harsit2", 20)


print(m.bucketSize)
# print(m.size())
# m.Insert("harsit", 30)
# print(m.size())
# # m.remove("harsit")
# m.Insert("harsiss", 10)
# print(m.search("harsit"))
# print(m.size())
