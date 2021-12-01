import queue 
class Graph:
    def __init__(self, numVer):
        self.numVer = numVer
        self.adjMatrix = [[0 for i in range(self.numVer)]for j in range(self.numVer)]
    

    def addEgde(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1]=1
    
    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] >0 else False
    
    def __str__(self):
        return str(self.adjMatrix)

    def DFShelper(self, sv, visited):
        print(sv);
        visited[sv] = True;
        for i in range(self.numVer):
            if(self.adjMatrix[sv][i] > 0 and visited[i] is False):
                self.DFShelper(i, visited)


    def DFS(self):
        visited = [False for v in range(self.numVer)]
        return self.DFShelper(0, visited)

    def BFS(self):
        visited = [False for i in range(self.numVer)];
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        while(not q.empty()):
            front = q.get()
            print(front);
            for i in range(self.numVer):
                if (self.adjMatrix[i][front] > 0 and visited[i] is False):
                    q.put(i);
                    visited[i] = True




g = Graph(4)
g.addEgde(0, 1)
g.addEgde(0, 2)
g.addEgde(1, 3)
g.addEgde(2 , 1)

g.BFS()
