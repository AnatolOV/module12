import logging
import unittest
from rt_with_exceptions import Runner, Tournament

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    filename='runner_tests.log',  # Название файла
    filemode='w',  # Режим записи с заменой
    encoding='utf-8',  # Кодировка
    format='%(levelname)s: %(message)s'  # Формат вывода
)


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_walk(self):
        try:
            t_runner = Runner('Andrey',speed=-5)
            for i in range(0,10):
                t_runner.walk()
            self.assertEqual(t_runner.distance,50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для Runner")
            raise ValueError

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_run(self):
        try:
            t_runner = Runner(777)
            for i in range(0,10):
                t_runner.run()
            self.assertEqual(t_runner.distance, 100)
            logging.info('Тест выполнен успешно')
            print(4)
        except TypeError:
            # print(9)
            logging.warning("Неверный тип данных для объекта Runner")
            raise TypeError

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')

    def test_challenge(self):
        t_runner1 = Runner('Andrey')
        t_runner2 = Runner('Nikita')
        for i in range(0,10):
            t_runner1.run()
            t_runner2.walk()
        self.assertNotEqual(t_runner1.distance,t_runner2.distance)