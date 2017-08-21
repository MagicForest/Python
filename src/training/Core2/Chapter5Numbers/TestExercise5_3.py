import unittest
import Exercise5_3

class TestExercise5_3(unittest.TestCase):
    def test_get_score_level_A(self):
        self.assertEquals('A', Exercise5_3.get_score_level(90))
        self.assertEquals('A', Exercise5_3.get_score_level(95))
        self.assertEquals('A', Exercise5_3.get_score_level(100))

    def test_get_score_level_B(self):
        self.assertEquals('B', Exercise5_3.get_score_level(80))
        self.assertEquals('B', Exercise5_3.get_score_level(85))
        self.assertEquals('B', Exercise5_3.get_score_level(89))

    def test_get_score_level_C(self):
        self.assertEquals('C', Exercise5_3.get_score_level(70))
        self.assertEquals('C', Exercise5_3.get_score_level(75))
        self.assertEquals('C', Exercise5_3.get_score_level(79))

    def test_get_score_level_D(self):
        self.assertEquals('D', Exercise5_3.get_score_level(60))
        self.assertEquals('D', Exercise5_3.get_score_level(65))
        self.assertEquals('D', Exercise5_3.get_score_level(69))

    def test_get_score_level_F(self):
        self.assertEquals('F', Exercise5_3.get_score_level(0))
        self.assertEquals('F', Exercise5_3.get_score_level(50))
        self.assertEquals('F', Exercise5_3.get_score_level(59))

    def test_get_score_level_raise_error(self):
        try:
            Exercise5_3.get_score_level(102)
            self.assertTrue(True)
        except ValueError , value_error:
           self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()