from collections import defaultdict

# define graph
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
       self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
       self.graph[u].append(v)

    #Reference: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    def DFS(self, s, path = []):
        if s not in path:
            path.append(s)
            for adjacent in self.graph[s]:
                self.DFS(adjacent, path)  
        return path

# Driver code
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v)
f.close()

g.DFS(1)

#Reference: https://www.w3schools.com/python/python_file_write.asp
h = open("output_DFS.txt", "w")
h.write(str(g.DFS(1)))

