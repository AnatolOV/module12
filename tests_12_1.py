import  unittest
import runner

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_walk(self):
        t_runner = runner.Runner('Andrey')
        for i in range(0,10):
            t_runner.walk()
        self.assertEqual(t_runner.distance,50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_run(self):
        t_runner = runner.Runner('Andrey')
        for i in range(0,10):
            t_runner.run()
        self.assertEqual(t_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_challenge(self):
        t_runner1 = runner.Runner('Andrey')
        t_runner2 = runner.Runner('Nikita')
        for i in range(0,10):
            t_runner1.run()
            t_runner2.walk()
        self.assertNotEqual(t_runner1.distance,t_runner2.distance)