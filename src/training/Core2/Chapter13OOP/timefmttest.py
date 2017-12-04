import unittest
import time
from timefmt import TimeFmt


class TimeFmtTest(unittest.TestCase):
    def test_create_default(self):
        self.assertAlmostEqual(TimeFmt().value, time.time(),delta=0.5)

    def test_update(self):
        time1 = TimeFmt()
        time1.update(1512426394.59)
        self.assertEqual(time1.value,1512426394.59)

    def test_display(self):
        time1 = TimeFmt(1512426394.59)
        self.assertEqual(time1.display("MDY"), "12/05/17")
        self.assertEqual(time1.display("MDYY"), "12/05/2017")
        self.assertEqual(time1.display("DMY"), "05/12/17")
        self.assertEqual(time1.display("DMYY"), "05/12/2017")
        self.assertEqual(time1.display("MODYY"), "Tue 05, 2017")
        self.assertEqual(time1.display(), "Tue Dec 05 06:26:34 2017")

if __name__ == '__main__':
    unittest.main()