from unittest import TestCase
from state.state import State


class FirebaseTestSuite(TestCase):

    def test_State(self):
        uuid = 'd1437765-TEST-4d1c-a8dc-adbf7d6bbded'
        state = State(uuid)
        state.read()
        state.insert()
        state.delete()




