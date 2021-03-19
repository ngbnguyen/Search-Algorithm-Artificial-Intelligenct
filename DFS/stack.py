class Stack:
    def __init__(self):
        self.__stack__ = []

    def push(self, item):
        self.__stack__.append(item)

    def pop(self):
        if len(self.__stack__) < 1:
            return None
        return self.__stack__.pop()

    def size(self):
        return len(self.__stack__)

    def front(self):
        first = self.__stack__[-1]
        return first
    
    def back(self):
        last = self.__stack__[0]
        return last

    def isEmpty(self):
        return self.__stack__ == []
    
    def print_s(self):
        return self.__stack__

pass