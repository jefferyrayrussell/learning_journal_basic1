import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'learning_journal_basic1')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from learning_journal_basic1 import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)

def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from .models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from .models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from .models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


# class TestMyViewSuccessCondition(BaseTest):

#     def setUp(self):
#         super(TestMyViewSuccessCondition, self).setUp()
#         self.init_database()

#         from .models import MyModel

#         model = MyModel(name='one', value=55)
#         self.session.add(model)

#     def test_passing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info['one'].name, 'one')
#         self.assertEqual(info['project'], 'jeff_learning_journal')


# class TestMyViewFailureCondition(BaseTest):

#     def test_failing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info.status_int, 500)