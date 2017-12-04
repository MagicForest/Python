import  unittest
from point import Point

class PointTest(unittest.TestCase):
    def test_create_default_point(self):
        p1 = Point()
        self.assertEqual(p1.x, 0.0)
        self.assertEqual(p1.y, 0.0)

    def test_create_normal_point(self):
        p1 = Point(1, 2)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 2)


if __name__ == '__main__':
    unittest.main()
