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

    # Reference: https://www.geeksforgeeks.org/a-search-algorithm/
    # function to be implemented
    def A_star(self, s, g, h):
        visited = [0] * n
        visited[0] = True
        founded_path= []
        frontier = [s]
       
        pq = PriorityQueue()
        pq.put((0, s))
        pq.put((h[s][0] , s))

        path_list = defaultdict()

        while pq.empty() == False:
            total_cost ,currentNode = pq.get()
            frontier.remove(currentNode)
            path = []
            path.append(currentNode)

            # Displaying the path having lowest heuristic
            #print(u, end=" ")

            if currentNode == g:   # check currentNode is goal node , then break
                break
            for v, l in self.graph[currentNode]:
                if visited[v] == False:
                    visited[v] = True
                    f_cost = l + total_cost + h[v][0] - h[u][0]  # calculate the f(n) = g(n) + h(n)
                    frontier.append(v)
                    pq.put((f_cost, v))
                path_list[v] = currentNode

        while g != s:               # find the path 
            for (key,parent) in path_list.items():
                if key == g:
                    founded_path.append(key)
                    g = parent
        founded_path.append(s)
        print("\n Founded path is ",founded_path[::-1])

        print("\n Total path cost = ", total_cost) 
        return total_cost
   

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
print(g.A_star(start, goal, heuristic))

# Reference: https://www.w3schools.com/python/python_file_write.asp
f = open("output.txt", "w")
f.write(str(g.A_star(start, goal, heuristic)))
f.close()