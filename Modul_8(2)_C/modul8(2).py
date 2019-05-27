print ("================NOMOR1=====================")
class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), "Antrian sedang kosong."
        return self.qlist.pop(0)
    def get_front_most(self):
        assert not self.is_empty(), "Antiran sedang kosong."
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), "Antrian sedang kosong."
        return self.qlist[-1]

Q = Queue()
Q.enqueue(28)
Q.enqueue(19)
Q.enqueue(45)
Q.enqueue(13)

print (Q.dequeue())
print (Q.dequeue())

print (Q.get_front_most())
print (Q.get_rear_most())

print ("=========================NOMOR2===================")
class PriorityQueue():
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def is_empty(self):
        return len (self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item

class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)

print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
