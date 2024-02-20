import unittest
from main import hello_world

class TestExercice1(unittest.TestCase):
    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
