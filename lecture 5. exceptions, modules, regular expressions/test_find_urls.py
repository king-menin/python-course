# -*- encoding: utf-8 -*-


import unittest

# rename the module for finding urls to "find_urls.py"
from find_urls import find_urls


class TestFindUrls(unittest.TestCase):
    def test_generic(self):
        self.assertListEqual(list(find_urls('http://ya.ru')), ['http://ya.ru'])
        self.assertListEqual(list(find_urls('http://www.ya.ru')),
                             ['http://www.ya.ru'])
        self.assertListEqual(list(find_urls('https://www.ya.ru')),
                             ['https://www.ya.ru'])
        self.assertListEqual(list(find_urls('abcdhttp://www.ya.ru')),
                             ['http://www.ya.ru'])
        self.assertListEqual(list(find_urls('http://www.ya.ru/dir')),
                             ['http://www.ya.ru/dir'])
        self.assertListEqual(list(find_urls('http://www.ya.ru/dir')),
                             ['http://www.ya.ru/dir'])
        self.assertListEqual(list(find_urls('hello www.yandex.ru')),
                             ['www.yandex.ru'])
        self.assertListEqual(list(find_urls('helloyandex.ru')), [])
        self.assertListEqual(list(find_urls('www.url-with-dash.com')),
                             ['www.url-with-dash.com'])
        self.assertListEqual(list(find_urls('www.not url.com')), [])
        self.assertListEqual(list(find_urls('http://www.ya.ru:80/dir')),
                             ['http://www.ya.ru:80/dir'])
        self.assertListEqual(list(find_urls('www.some.ru/path.php')),
                             ['www.some.ru/path.php'])


if __name__ == '__main__':
    unittest.main()
