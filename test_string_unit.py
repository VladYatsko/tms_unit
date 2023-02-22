import unittest
from unittest import TestCase


class TestStringMethods(TestCase):
    
    def setUp(self):
        print("\nset up")
        
    def tearDown(self):
        print("\ntear down")

    def test_upper(self):
        print("upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("is upper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
    