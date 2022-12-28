import unittest
from name_function import get_formatted_name2

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like 'janis joplin' work?"""
        # This is what the function is taking in as an example and comparing
        formatted_name = get_formatted_name2('janis', 'joplin')
        # Assert methods verify that the result you received is the same as the result you were expecting
        # We know we are supposed to receive 'Janis Joplin' capitalized because we have the title() in name_function so it compares
        # This answer to the answer in the other file
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()