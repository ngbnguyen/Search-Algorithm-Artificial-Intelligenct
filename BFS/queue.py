class Queue:
    def __init__(self):
        self.__queue__ = []

    def enqueue(self, item):
        self.__queue__.append(item)

    def dequeue(self):
        if len(self.__queue__) < 1:
            return None
        return self.__queue__.pop(0)

    def size(self):
        return len(self.__queue__)

    def front(self):
        first = self.__queue__[0]
        return first
    
    def back(self):
        last = self.__queue__[-1]
        return last

    def isEmpty(self):
        return self.__queue__ == []

    def print_q(self):
        return self.__queue__
pass