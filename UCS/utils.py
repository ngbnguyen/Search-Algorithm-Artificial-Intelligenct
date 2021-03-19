import heapq
class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self._queue = []
        pass

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item)) 
        pass

    def pop(self):
        return heapq.heappop(self._queue)
        pass

    def isEmpty(self):
        return not self._queue
        
    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        flag = 0 
        for (p, i) in self._queue:
            if i == item: 
                flag = 1 
                if p >= priority:
                    return 
                elif p < priority:
                    self._queue.remove((p,i))
                    self.push(item,priority)
        if flag == 0:  
            self.push(item,priority) 
        pass



q = PriorityQueue()
print(q.isEmpty())

q.push(1,2)
q.push(2,3)
q.push(3,4)

q.update(1,3)

print(q.isEmpty())
while not q.isEmpty(): 
    print(q.pop())

print ("++++++++++++")
q.push(1,2)
q.push(2,3)
q.push(3,4)

q.update(1,2)

print(q.isEmpty())
while not q.isEmpty(): 
    print(q.pop())
#ref :https://towardsdatascience.com/priority-queues-in-python-3baf0bac2097