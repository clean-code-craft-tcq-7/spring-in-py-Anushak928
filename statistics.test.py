import unittest
import math
import statistics  
class StatsTest(unittest.TestCase):
    def test_report_min_max_avg(self):
        computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

    def test_avg_is_nan_for_empty_input(self):
        computedStats = statistics.calculateStats([])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["min"]))
        self.assertTrue(math.isnan(computedStats["max"]))

    def test_single_element_list(self):
        computedStats = statistics.calculateStats([5.0])
        self.assertEqual(computedStats["avg"], 5.0)
        self.assertEqual(computedStats["min"], 5.0)
        self.assertEqual(computedStats["max"], 5.0)

    def test_negative_numbers(self):
        computedStats = statistics.calculateStats([-1.0, -3.5, -2.2])
        self.assertEqual(computedStats["min"], -3.5)
        self.assertEqual(computedStats["max"], -1.0)
        self.assertAlmostEqual(computedStats["avg"], -2.233, delta=0.001)

    def test_identical_numbers(self):
        computedStats = statistics.calculateStats([2.2, 2.2, 2.2])
        self.assertEqual(computedStats["avg"], 2.2)
        self.assertEqual(computedStats["min"], 2.2)
        self.assertEqual(computedStats["max"], 2.2)

    def test_floating_point_precision(self):
        computedStats = statistics.calculateStats([0.1, 0.2, 0.3])
        self.assertAlmostEqual(computedStats["avg"], 0.2, delta=0.00001)
        self.assertAlmostEqual(computedStats["min"], 0.1, delta=0.00001)
        self.assertAlmostEqual(computedStats["max"], 0.3, delta=0.00001)


if __name__ == "__main__":
    unittest.main()
