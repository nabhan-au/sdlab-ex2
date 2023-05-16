import unittest
from speciallecture.CSVPrinter import CSVPrinter


def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownModule')


class test_CSVPrinter_with_right_file(unittest.TestCase):

    printer: CSVPrinter


    @classmethod
    def setUpClass(cls):
        print('Running CSVPrinter_with_right_file setUpClass')
        cls.printer = CSVPrinter("sample.csv")

    @classmethod
    def tearDownClass(cls):
        print('Running CSVPrinter_with_right_file tearDownClass')

    def setUp(self):
        print('Running CSVPrinter_with_right_file setUp')

    def tearDown(self):
        print('Running CSVPrinter_with_right_file tearDown')

    def test_read(self):
        l = self.printer.read()
        self.assertEqual(3, len(l))

    def test_separate_element(self):
        line = self.printer.read()
        self.assertEqual(" value2B", line[1][1])


class test_CSVPrinter_with_wrong_file(unittest.TestCase):

    printer: CSVPrinter

    @classmethod
    def setUpClass(cls):
        print('Running CSVPrinter_with_wrong_file setUpClass')
        cls.printer = CSVPrinter("")

    @classmethod
    def tearDownClass(cls):
        print('Running CSVPrinter_with_wrong_file tearDownClass')

    def setUp(self):
        print('Running CSVPrinter_with_wrong_file setUp')

    def tearDown(self):
        print('Running CSVPrinter_with_wrong_file tearDown')


    def test_file_exist(self):
        self.assertRaises(Exception, self.printer.read)
