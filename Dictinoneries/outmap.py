class MapNode:
    def __init__(self, key, value):
        self.key = key;
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 20
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0;
    
    def size(self):
        return self.count
    
    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketSize))

    def Insert(self, key, value):
        hc = hash(key)
        bucketIndex = self.getBucketIndex(hc)
        head = self.bucket[bucketIndex]
        while head!=None:
            if head.key == key:
                head.value = value
                return 
            head = head.next

        head = self.bucket[bucketIndex]
        newnode = MapNode(key, value)
        newnode.next = head
        self.bucket[bucketIndex] = newnode
        self.count+=1
    

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
print(m.size())
m.Insert("harsit", 30)
print(m.size())
# m.remove("harsit")
m.Insert("harsiss", 10)
print(m.search("harsit"))
print(m.size())
