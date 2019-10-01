from app import app
import unittest

class AppTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

if __name__ == "__main__":
    unittest.main()
