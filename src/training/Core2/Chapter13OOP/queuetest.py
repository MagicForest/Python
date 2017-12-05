import unittest
from queue import Queue


class QueueTest(unittest.TestCase):
    def test_is_empty(self):
        queue1 = Queue()
        self.assertTrue(queue1.isEmpty())
        queue1.enQueue(1)
        self.assertFalse(queue1.isEmpty())

    def test_enQueue_deQueue(self):
        queue1 = Queue()
        queue1.enQueue(1)
        queue1.enQueue(2)
        self.assertEqual(queue1.deQueue(), 1)
        self.assertEqual(queue1.deQueue(), 2)
        self.assertTrue(queue1.isEmpty())


if __name__ == '__main__':
    unittest.main()
