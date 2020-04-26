from unittest import TestCase
from streams.streams import Stream
from token_utils.token import get_test_access


class StreamsTestSuite(TestCase):

    def test_refresh(self):
        stream = Stream(get_test_access())
        r = stream.get_stream(3345238805)
        self.assertEqual(r['heartrate']['data'][3], 80)
