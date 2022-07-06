from cgi import test
import unittest
from log_pain import get_body_part

class LogPainTestCase(unittest.TestCase):
    """Test for 'log_pain.py'"""

    def test_get_body_part(self):
        """Can you get a proper value?"""
        test_return_value = get_body_part(1)
        self.assertEqual(test_return_value, 'niska')

if __name__ == '__main__':
    unittest.main()
    