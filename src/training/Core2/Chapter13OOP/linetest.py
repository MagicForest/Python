import unittest
from point import Point
from line import Line


class LineTest(unittest.TestCase):
    def test_create_line(self):
        line1 = Line(Point(),Point(1,0),1,0)
        self.assertEqual(repr(line1),'((0.0,0.0),(1.0,0.0))')
        self.assertEqual(line1.length, 1.0)
        self.assertEqual(line1.slope, 0)


if __name__ == '__main__':
    unittest.main()
