class Stack(object):
    'exercise 13-8'
    def __init__(self):
        self.value = []

    def push(self, e):
        self.value.append(e)

    def isEmpty(self):
        return 0 == len(self.value)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.value[-1]

    def pop(self):
        return self.value.pop()
