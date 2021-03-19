from collections import defaultdict
from os import close

# define graph
class Graph:

    # Constructor
   def __init__(self):
        # default dictionary to store graph
       self.graph = defaultdict(list)

    # function to add an edge to graph
   def addEdge(self, u, v):
       self.graph[u].append(v)

    #Reference: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
   # function to be implemented
   def BFS(self, s):
        #Make path 
        path = " "
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
 
            # Dequeue a vertex from 
            # queue 
            s = queue.pop(0)
            path += str(s) + " "
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return path.rstrip()
# Driver code
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v)
f.close()

g.BFS(1)

# Reference: https://www.w3schools.com/python/python_file_write.asp
h = open("output_BFS.txt", "w")
h.write(str(g.BFS(1)))
h.close()
