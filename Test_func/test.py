import unittest
from name_func import get_formatted_name

class NamesTest(unittest.TestCase):
    def test_name(self):
        formatted_name=get_formatted_name('roy', 'dai')
        self.assertEqual(formatted_name,'Roy Dai')

if __name__=='__main__':
    unittest.main()