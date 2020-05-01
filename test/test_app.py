from unittest import TestCase

from app import create_app
from werkzeug.http import parse_cookie
from state.state import State

TEST_DB = 'test.db'


class AppTestSuite(TestCase):
    """App cases."""

    # executed prior to each test
    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #                                         os.path.join(
        #                                             app.config['BASEDIR'],
        #                                             TEST_DB)

        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        cookies = response.headers.getlist('Set-Cookie')
        name = 'state'
        for cookie in cookies:
            for c_key, c_value in parse_cookie(cookie).items():
                if c_key == name:
                    state = State(c_value)
                    self.assertEqual(c_value, state.state)
                    state.delete()
                    print(c_value)

        self.assertEqual(response.status_code, 200)

    def test_main_session(self):
        with self.app.session_transaction() as session:
            session['state'] = 'test'

        response = self.app.get('/', follow_redirects=True)
        cookies = response.headers.getlist('Set-Cookie')
        name = 'state'
        for cookie in cookies:
            for c_key, c_value in parse_cookie(cookie).items():
                if c_key == name:
                    state = State(c_value)
                    self.assertEqual(c_value, state.state)
                    state.delete()
                    print(c_value)
        self.assertEqual(response.status_code, 200)
