from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest
import unittest

testSuit = unittest.TestSuite()
testSuit.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
testSuit.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# print(testSuit)
if __name__ == "__main__":
    # Создаем экземпляр TextTestRunner с ответом verbosity=2
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testSuit)
