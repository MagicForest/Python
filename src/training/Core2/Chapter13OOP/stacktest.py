import unittest
from stack import Stack


class StackTest(unittest.TestCase):
    def test_is_empty(self):
        stack1 = Stack()
        self.assertTrue(stack1.isEmpty())
        stack1.push(1)
        self.assertFalse(stack1.isEmpty())

    def test_push(self):
        stack1 = Stack()
        self.assertEqual(stack1.peek(), None)
        stack1.push(1)
        self.assertEqual(stack1.peek(), 1)
        stack1.push(2)
        self.assertEqual(stack1.peek(), 2)

    def test_pop(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        self.assertEqual(stack1.pop(), 3)
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.pop(), 1)
        self.assertTrue(stack1.isEmpty())


if __name__ == '__main__':
    unittest.main()