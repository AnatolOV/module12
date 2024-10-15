import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_tournament1(self):
        tour_ = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results = tour_.start()
        # print(self.__class__.all_results)
        self.assertTrue(self.__class__.all_results[2] == 'Ник')

    def test_tournament2(self):
        tour_ = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results = tour_.start()
        self.assertTrue(self.__class__.all_results[2] == 'Ник')


    def test_tournament3(self):
        tour_ = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results = tour_.start()
        self.assertTrue(self.__class__.all_results[3] == 'Ник')

