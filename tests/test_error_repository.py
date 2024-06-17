import unittest

from error_repository import ErrorRepository

class TestErrorRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ErrorRepository()
        self.repo.add_error(1, "Ошибка доступа")
        self.repo.add_error(2, "Файл не найден")

    def test_known_error(self):
        self.assertEqual(self.repo.translate(1), "Ошибка доступа")

    def test_unknown_error(self):
        self.assertEqual(self.repo.translate(3), "Unknown error")

if __name__ == '__main__':
    unittest.main()