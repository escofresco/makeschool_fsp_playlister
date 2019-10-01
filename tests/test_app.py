from app import app
import unittest

class AppTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_view(self):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Playlist', result.data)

    def test_new(self):
        """Test the new playlist creation page."""
        result = self.client.get('/playlists/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Playlist', result.data)

if __name__ == "__main__":
    unittest.main()
