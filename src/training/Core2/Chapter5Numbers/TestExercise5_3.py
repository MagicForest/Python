import unittest
import Exercise5_3

class TestExercise5_3(unittest.TestCase):
    def test_getScoreLevel_A(self):
        self.assertEquals('A', Exercise5_3.getScoreLevel(90))
        self.assertEquals('A', Exercise5_3.getScoreLevel(95))
        self.assertEquals('A', Exercise5_3.getScoreLevel(100))
    def test_getScoreLevel_B(self):
        self.assertEquals('B', Exercise5_3.getScoreLevel(80))
        self.assertEquals('B', Exercise5_3.getScoreLevel(85))
        self.assertEquals('B', Exercise5_3.getScoreLevel(89))
    def test_getScoreLevel_C(self):
        self.assertEquals('C', Exercise5_3.getScoreLevel(70))
        self.assertEquals('C', Exercise5_3.getScoreLevel(75))
        self.assertEquals('C', Exercise5_3.getScoreLevel(79))
    def test_getScoreLevel_D(self):
        self.assertEquals('D', Exercise5_3.getScoreLevel(60))
        self.assertEquals('D', Exercise5_3.getScoreLevel(65))
        self.assertEquals('D', Exercise5_3.getScoreLevel(69))
    def test_getScoreLevel_F(self):
        self.assertEquals('F', Exercise5_3.getScoreLevel(50))

if __name__ == '__main__':
    unittest.main()