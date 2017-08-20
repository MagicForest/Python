import unittest
import  Exercise5_6

class TestExercise5_6(unittest.TestCase):
    def test_add(self):
       params = Exercise5_6.parseExpression('1+2')
       self.assertEquals(3, Exercise5_6.calculate(params['firstOperand'],params['operator'], params['secondOperand']))

if __name__ == '__main__':
    unittest.main()