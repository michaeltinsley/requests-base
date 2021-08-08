import unittest

from requests_base import BaseUrlSession


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.CORRECT_BASE_URL = "https://jsonplaceholder.typicode.com/"
        self.INCORRECT_BASE_URL = "https://jsonplaceholder.typicode.com"

        self.CORRECT_URL = "todos/"
        self.INCORRECT_URL = "/todos"

    def test_with_correct_base_correct_url(self):
        session = BaseUrlSession(
            base_url=self.CORRECT_BASE_URL,
        )
        response = session.get(url=self.CORRECT_URL)
        response.raise_for_status()

    def test_with_incorrect_base_correct_url(self):
        session = BaseUrlSession(
            base_url=self.INCORRECT_BASE_URL,
        )
        response = session.get(url=self.CORRECT_URL)
        response.raise_for_status()

    def test_with_correct_base_incorrect_url(self):
        session = BaseUrlSession(
            base_url=self.CORRECT_BASE_URL,
        )
        response = session.get(url=self.INCORRECT_URL)
        response.raise_for_status()

    def test_with_incorrect_base_incorrect_url(self):
        session = BaseUrlSession(
            base_url=self.INCORRECT_BASE_URL,
        )
        response = session.get(url=self.INCORRECT_URL)
        response.raise_for_status()


if __name__ == "__main__":
    unittest.main()
