from unittest import TestCase
from bigQuery.bigQuery import BigQ


class BigQTestSuite(TestCase):

    def test_time(self):
        bigQ = BigQ()
        print(bigQ.getTime())


