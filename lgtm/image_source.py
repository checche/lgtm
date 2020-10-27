import requests
from io import BytesIO
from pathlib import Path
import random


class LocalImage():
    """ローカルの画像を取得する"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')


class RemoteImage():
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """LoremFlickrからキーワード検索し、画像を取得する"""

    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (
            f'{self.LOREM_FLICKR_URL}/'
            f'{self.WIDTH}/{self.HEIGHT}/{keyword}'
        )


# LoremFlickrを使わなくなればここを差し替えれば良い
KeywordImage = _LoremFlickr


class GhibliImage(RemoteImage):
    GHIBRI_URL = 'http://www.ghibli.jp/gallery/'
    TITLES = ['karigurashi', 'chihiro']
    FORMAT = '.jpg'

    def __init__(self):
        super().__init__(self._build_url())

    def _build_url(self):
        title = random.choice(self.TITLES)
        number = str(random.randint(1, 50)).zfill(3)
        return (
            f'{self.GHIBRI_URL}{title}{number}{self.FORMAT}'
        )


def ImageSource(keyword):
    """最適なイメージソースのインスタンスを返す

    Args:
        keyword (str): URL or local_path or query
    """

    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    elif keyword == 'ghibli':
        return GhibliImage()
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """[summary]

    Args:
        keyword (str): キーワード(URL or local_path or query)

    Returns:
        _io.BytesIO | _io.BufferedReader : ファイルオブジェクト
    """
    return ImageSource(keyword).get_image()
