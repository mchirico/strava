from unittest import TestCase
from token_utils.token import Token
from flask import request


class TokenTestSuite(TestCase):

    def test_token(self):
        token = Token(request)
        self.assertFalse(token.status)



