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

   # function to be implemented
   def BFS(self, s, end):
        
       # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append([s])
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from 
            # queue and print it
            path = queue.pop(0)
            node = path[-1]
            # PRINT PATH
            print("Entries: ",path)
            for count, i in enumerate(visited):
                if i == True:
                    for key, value in self.graph.items():
                        if str(count) == str(key):
                            print(key)
            if node == end:
                return path

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[path[-1]]:
                if visited[i] == False:
                    new_path = list(path)
                    new_path.append(i)
                    queue.append(new_path)
                    visited[i] = True
            # for adjacent in graph.get(node, []):
            #     new_path = list(path)
            #     new_path.append(adjacent)
            #     queue.append(new_path)
 

# Driver code
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u, v)
f.close()

print(g.BFS(1, 6))

h = open("output.txt", "w")
h.write(str(g.BFS(1,6)))
h.close() 
#Ref: https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search