
# import pytest
# import transaction
# import datetime
# from ..views.default import TIME_FORMAT

# from pyramid import testing

# from .models import (
#     MyModel,
#     get_engine,
#     get_session_factory,
#     get_tm_session,
# )
# from .models.meta import Base

# DB_SETTINGS = {'sqlalchemy.url': 'sqlite:////tmp/testme.sqlite'}


# @pytest.fixture(scope="session")
# def sqlengine(request):
#     """Set up sql engine for testing."""
#     config = testing.setUp(settings=DB_SETTINGS)
#     config.include(".models")
#     settings = config.get_settings()
#     engine = get_engine(settings)
#     Base.metadata.create_all(engine)


#     def teardown():
#         testing.tearDown()
#         transaction.abort()
#         Base.metadata.drop_all(engine)

#     request.addfinalizer(teardown)
#     return engine


# @pytest.fixture(scope="function")
# def new_session(sqlengine, request):
#     """Set up new session for testing."""
#     session_factory = get_session_factory(sqlengine)
#     session = get_tm_session(session_factory, transaction.manager)

#     def teardown():
#         transaction.abort()

#     request.addfinalizer(teardown)
#     return session


# @pytest.fixture(scope="function")
# def populated_db(request, sqlengine):
#     """Set up mock database for testing."""
#     session_factory = get_session_factory(sqlengine)
#     session = get_tm_session(session_factory, transaction.manager)

#     with transaction.manager:
#         session.add(MyModel(title="Purgatory", body="The reality of pythonic purgatory cannot be denied.", date=datetime.datetime.utcnow()))

#     def teardown():
#         with transaction.manager:
#             session.query(MyModel).delete()

#     request.addfinalizer(teardown)


# @pytest.fixture()
# def dummy_request(new_session):
#     """Testing a dummy request."""
#     return testing.DummyRequest(dbsession=new_session)


# def test_home_view(dummy_request, new_session):
#     """Test entries are in home view."""
#     from .views.default import home_view
#     new_session.add(MyModel(title="test", body="this is a test", date=datetime.strptime(entry['date'], TIME_FORMAT)))
#     new_session.flush()
#     info = home_view(dummy_request)
#     assert "entries" in info


# def test_detail_view(new_session):
#     """Test detail view has a body."""
#     from .views.default import detail_view
#     request = testing.DummyRequest(dbsession=new_session)
#     new_session.add(MyModel(title="test", body="this is a test", date=datetime.strptime(entry['date'], TIME_FORMAT)))
#     new_session.flush()
#     request.matchdict = {'id': '1'}
#     info = detail_view(request)
#     assert "this is a test" in info['entry'].body


# def test_entry_view():
#     """Test entry view."""
#     from .views.default import entry_view
#     request = testing.DummyRequest()
#     entry_view(request)
#     assert request.response.status_code == 200


# def test_edit_view(new_session):
#     """Test update view has a body."""
#     from .views.default import edit_view
#     request = testing.DummyRequest(dbsession=new_session)
#     new_session.add(MyModel(title="test", body="this is a test", date=datetime.strptime(entry['date'], TIME_FORMAT)))
#     new_session.flush()
#     request.matchdict = {'id': '1'}
#     info = edit_view(request)
#     assert info["entry"].body == "this is a test"

# # -------Functional Tests----------


# @pytest.fixture()
# def testapp(sqlengine):
#     """Setting Up TestApp."""
#     from learning_journal_basic1 import main
#     app = main({}, **DB_SETTINGS)
#     from webtest import TestApp
#     return TestApp(app)


# def test_layout_root_home(testapp, populated_db):
#     """Test layout root of home route."""
#     response = testapp.get('/', status=200)
#     assert b'Purgatory' in response.body


# def test_layout_root_entry(testapp):
#     """Test layout root of entry route."""
#     response = testapp.get('/journal/new_entry', status=200)
#     assert response.html.find("textarea")


# def test_layout_root_edit(testapp, populated_db):
#     """Test layout root of edit route."""
#     response = testapp.get('/journal/edit_view/{id:\d+}', status=200)
#     html = response.html
#     assert html.find("h2")


# def test_layout_root_detail(testapp, populated_db):
#     """Test layout root of detail route."""
#     response = testapp.get('/detail/1', status=200)
#     html = response.html
#     assert html.find("p")


# def test_root_contents_home(testapp, populated_db):
#     """Test contents of root page contain as many <article> as journal entries."""
#     response = testapp.get('/', status=200)
#     html = response.html
#     assert len(html.findAll("article")) == 1


# def test_root_contents_create_notitle(testapp):
#     """Test no title returns dictionary with error."""


# def test_root_contents_detail(testapp, populated_db):
#     """Test contents of detail page contains <p> in detail content."""
#     response = testapp.get('/detail/1', status=200)
#     assert b"The reality of pythonic purgatory cannot be denied." in response.body
