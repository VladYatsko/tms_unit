import unittest
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):
    
    def setUp(self):
        self.first = Triangle(9, 8, 7)
        self.second = Triangle(8, 7, 10)
        
    def tearDown(self):
        del self.first
        del self.second
 
    def test_triangle_eq(self):
        third = Triangle(9, 8, 7)
        self.assertEqual(self.first, third)
        
    def test_triangle_nq(self):
        self.assertNotEqual(self.first, self.second)
        
    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(),
                         self.first.a + self.first.b + self.first.c)
        
    def test_less_than(self):
        third = Triangle(10, 11, 12)
        self.assertLess(self.first, third)
        
    def test_greater_than(self):
        third = Triangle(10, 11, 12)
        self.assertGreater(third, self.first)
        
    def test_square(self):
        self.assertEqual(int(self.first.square()), int(26.832815729997478))
    
    def test_del(self):
        self.assertIsNone(self.first.__del__())
        
        