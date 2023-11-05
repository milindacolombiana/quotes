import unittest
import requests

from handler import main_handler


class TestMainHandler(unittest.TestCase):
    def test_main_handler(self):
        res = main_handler(None, None)
        self.assertEqual(res.get("statusCode"), requests.codes.get("ok"))

