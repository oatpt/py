class queue:
    def __init__(self) :
        self.queue=[]
    def enQueue(self,valu):
        self.queue.append(valu)
    def deQueue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return self.queue==[]
    def size(self):
        return len(self.queue)
