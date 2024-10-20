import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    is_frozen = True

    # @classmethod
    # def setUpClass(cls):
    #     cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)
        self.all_results = {}

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    # @classmethod
    # def tearDownClass(cls):
    #     print(cls.all_results)
    #     for key, value in cls.all_results.items():
    #         print(f"{key}: {value}")
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")

    def test_tournament1(self):
        tour_ = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results = tour_.start()
        # print(self.__class__.all_results)
        self.assertTrue(self.all_results[2] == 'Ник')
        print(self.all_results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")

    def test_tournament2(self):
        tour_ = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results = tour_.start()
        self.assertTrue(self.all_results[2] == 'Ник')
        print(self.all_results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")

    def test_tournament3(self):
        tour_ = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = tour_.start()
        self.assertTrue(self.all_results[3] == 'Ник')
        print(self.all_results)
