from unittest import TestCase
from storage.storage import Buckets


class BigQTestSuite(TestCase):

    def test_quick(self):
        s = Buckets()
        files = s.upload()
        print(files)

    def test_createFromString(self):
        file = '/a/b/c/junk.txt'
        data = b'data'
        s = Buckets()
        s.createFromString(file, data)

        result = s.readFromString(file)
        self.assertEqual(result, data)
        print(data)

    def test_list(self):
        s = Buckets()
        print(s.list('/a'))

