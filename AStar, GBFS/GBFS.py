from collections import defaultdict
from queue import PriorityQueue

# define graph
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, l):
        self.graph[u].append((v, l))

    # Reference: https://www.geeksforgeeks.org/best-first-search-informed-search/
    # function to be implemented
    def GBFS(self, s, g, h):
        visited = [0] * n
        visited[0] = True
        heu = 0
        founded_path= []

       
        pq = PriorityQueue()
        pq.put((0, s))
        
        path_list = defaultdict()

        while pq.empty() == False:
            currentNode = pq.get()[1]
            path = []
            path.append(currentNode)
            # Displaying the path having lowest heuristic
            #print(u, end=" ")

            if currentNode == g:   # check currentNode is goal node , then break
                break
            for v, l in self.graph[currentNode]:
                if visited[v] == False:
                    visited[v] = True
                    a = h[v][0]
                    pq.put((a, v))
                path_list[v] = currentNode

        while g != s:               # find the path 
            for (key,parent) in path_list.items():
                if key == g:
                    founded_path.append(key)
                    g = parent
        founded_path.append(s)
        print("\n Founded path is ",founded_path[::-1])

        for i in founded_path:   # count the total heuristic 
            heu += h[i][0]
        print("\nTotal heuristic = ", heu)
        return heu
   

# Driver code
# Create a graph given in the above diagram
g = Graph()
heuristic = []

with open('input.txt', 'r') as f:
    n, m = [int(x) for x in next(f).split()]
    for i in range(m):
        u, v, l = [int(x) for x in next(f).split()]
        g.addEdge(u, v, l)
    for i in range(n):
        h = [int(x) for x in next(f).split()]
        heuristic.append(h)
    start, goal = [int(x) for x in next(f).split()]
f.close()
print(g.GBFS(start, goal, heuristic))

# Reference: https://www.w3schools.com/python/python_file_write.asp
f = open("output.txt", "w")
f.write(str(g.GBFS(start, goal, heuristic)))
f.close()