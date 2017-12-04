import unittest
from moneyfmt import MoneyFmt

class MoneyFmtTest(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(MoneyFmt(1234567.8901)), '$1,234,567.89')
        self.assertEqual(str(MoneyFmt(567.8901)), '$567.89')

    def test_update(self):
        fmt = MoneyFmt(1.33)
        self.assertEqual(str(fmt), '$1.33')

        fmt.update(100.234)
        self.assertEqual(str(fmt), '$100.23')

    def test_nonzero(self):
        self.assertEqual(str(MoneyFmt(0.5)), '$0.50')
        self.assertEqual(str(MoneyFmt()), '$0.00')

if __name__ == '__main__':
    unittest.main()
