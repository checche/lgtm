from tempfile import TemporaryDirectory
import unittest
from lgtm.image_source import (
    get_image, ImageSource, KeywordImage, LocalImage, RemoteImage
)


class ImageSourceTest(unittest.TestCase):
    def test_url(self):
        keyword = 'https://example.com'
        expected = RemoteImage(keyword)
        actual = ImageSource(keyword)

        self.assertEqual(type(actual), type(expected))

    def test_path(self):
        keyword = './tests/fixtures/test.png'
        expected = LocalImage(keyword)
        actual = ImageSource(keyword)
        self.assertEqual(type(actual), type(expected))

    def test_query(self):
        keyword = 'cat'
        expected = KeywordImage(keyword)
        actual = ImageSource(keyword)

        self.assertEqual(type(actual), type(expected))
