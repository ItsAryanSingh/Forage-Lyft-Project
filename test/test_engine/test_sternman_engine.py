import unittest
from engine.sternman_engine import SternmanEngine

class SternmanEngineTest(unittest.TestCase):

    def test_sternman_engine_expect_false(self):
        warning_light = False
        self.assertFalse(SternmanEngine(warning_light).needs_service())

    def test_sternman_engine_expect_true(self):
        warning_light = True
        self.assertTrue(SternmanEngine(warning_light).needs_service())