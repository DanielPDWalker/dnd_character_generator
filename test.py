from dnd_stat_rolls import character_creation_rolls
import unittest


class character_creation_rolls_test(unittest.TestCase):
    
    def setUp(self):
        self.big_test_runs = 10000
        self.small_test_runs = 10

    def test_6_stats_returned(self):
        returned_character_stats = character_creation_rolls()
        self.assertEqual(len(returned_character_stats), 6)

    def test_no_roll_over_18(self):
        for i in range(1, self.big_test_runs):
            returned_character_stats = character_creation_rolls()
            for i in returned_character_stats:
                self.assertLess(i, 19)
    
    def test_can_roll_an_18(self):
        check_int = 0
        for i in range(1, self.big_test_runs):
            returned_character_stats = character_creation_rolls()
            for i in returned_character_stats:
                if i > check_int:
                    check_int = i
        
        self.assertEqual(check_int, 18)


if __name__ == '__main__':
    unittest.main()
