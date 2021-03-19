from collections import defaultdict
from utils import PriorityQueue

#*define graph
class Graph:

    #*Constructor
    def __init__(self):
        #*Default dictionary to store graph
        self.graph = defaultdict(list)

    #*Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    #*Function to be implemented
    def UCS(self, s):
        pq = PriorityQueue()
        visited = []
        visited.append(s)
        for v, w in self.graph[s]:
            pq.update(item=v, priority=w)
            
        while not pq.isEmpty():
            (pri,it) = pq.pop()
            visited.append(it)
            for v,w in self.graph[it]:
                if  v not in visited:
                    pq.update(item=v, priority=w+pri)
        print(visited)

#*Driver code
#*Create a graph given in the above diagram
g = Graph()

#*Read from input file
f = open("input.txt", "r")
for line in f:
    u, v, w = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v, w)
f.close()

g.UCS(0)

