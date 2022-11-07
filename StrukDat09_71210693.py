class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
        self._size = 0
    
    def __len__ (self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def add(self, new, priority):
        if self.isEmpty():
            self._data.append((new, priority))
        else:
            bantu = 0
            while self._data[bantu][1] < priority:
                    bantu += 1
            self._data.insert(bantu, (new, priority))

    def update(self, priority, new):
        bantu = 0 
        while self._data[bantu][1] != priority:
                bantu += 1
        self._data[bantu] = (new, priority)

    def remove(self):
        self._data.pop(0)

    def peek(self):
        print("Data prioritas tertinggi: ", self._data[0])

    def removePriority(self, priority):
        bantu = 0 
        while self._data[bantu][1] != priority:
                bantu += 1
        self._data.pop(bantu)

    def printIsiQueue(self):
        print("Isi Semua Queue: ", end="")
        for i in range(0, len(self._data)-1):
            print((self._data[i]), end = ", ")
        print(self._data[-1])

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()