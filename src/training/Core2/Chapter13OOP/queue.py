class Queue(object):
    def __init__(self):
        self.value = []

    def enQueue(self,e):
        self.value.append(e)

    def isEmpty(self):
        return 0 == len(self.value)

    def deQueue(self):
        return self.value.pop(0)