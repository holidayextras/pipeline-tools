import unittest
import pipelinetools.logger as pl
import os
import mox

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))


class TestGenerator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None

    def setUp(self):
        self.mox = mox.Mox()
        self.result = unittest.TestResult()
        self.logger_class = 'Logger'

    def tearDown(self):
        # In case one of our tests fail before UnsetStubs is called.
        self.mox.UnsetStubs()

    def test_config(self):
        result = pl.init_a_logger()
        self.assertEqual(result.name, 'pipelinetool')