class Point(object):
    'exercise 13-5'
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%.1f,%.1f)' % (self.x,self.y)