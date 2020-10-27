import unittest
from lgtm.image_source import (
    _LoremFlickr, ImageSource, KeywordImage, LocalImage, RemoteImage
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


class LoremFlickrTest(unittest.TestCase):
    lorem_flickr = _LoremFlickr('cat')

    def test_build_url(self):
        actual = self.lorem_flickr._build_url('cat')

        expected = (
            f'{self.lorem_flickr.LOREM_FLICKR_URL}/'
            f'{self.lorem_flickr.WIDTH}/{self.lorem_flickr.HEIGHT}/cat'
        )

        self.assertEqual(actual, expected)

    def test_init(self):
        actual = self.lorem_flickr._url

        expected = (
            f'{self.lorem_flickr.LOREM_FLICKR_URL}/'
            f'{self.lorem_flickr.WIDTH}/{self.lorem_flickr.HEIGHT}/cat'
        )

        self.assertEqual(actual, expected)
