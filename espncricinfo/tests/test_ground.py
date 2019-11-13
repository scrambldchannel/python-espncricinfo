import unittest
from espncricinfo.ground import Ground

class TestMatchMethods(unittest.TestCase):

    def setUp(self):
        id = 57129
        self.ground = Ground(id)

    def test_ground_description(self):
        self.assertEqual(self.ground.short_name, "Lord's, London")

    def test_ground_country(self):
        self.assertEqual(self.ground.country, 'England')

    def test_first_test_match_id(self):
        self.assertEqual(self.ground.first_test.get('match_id'), 62410)

if __name__ == '__main__':
    unittest.main()
