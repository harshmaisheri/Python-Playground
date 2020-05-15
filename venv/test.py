import unittest
import randomgame


class UnitTest(unittest.TestCase):
    def test1(self):
        result = randomgame.guess_game(8, 8)
        self.assertTrue(result)

    def test2(self):
        result = randomgame.guess_game(1, 5)
        self.assertFalse(result)

    def test3(self):
        result = randomgame.guess_game(0, 5)
        self.assertFalse(result)

    def test4(self):
        result = randomgame.guess_game("1", 5)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
