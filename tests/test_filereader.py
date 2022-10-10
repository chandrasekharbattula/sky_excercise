import unittest
from unittest import TestCase

from main.filereader import TextFileReader


class TestTextFileReader(TestCase):
    def test_read(self):
        file_content = TextFileReader().read("data/calls.log")
        self.assertEqual(len(file_content), 6)


if __name__ == '__main__':
    unittest.main()
