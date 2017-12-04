from point import Point


class Line(object):
    'exercise 13-6'
    def __init__(self,p1,p2,length,slope):
        self.p1 = p1
        self.p2 = p2
        self.length = length
        self.slope = slope

    def __repr__(self):
        return '(%s,%s)' % (repr(self.p1), repr(self.p2))
