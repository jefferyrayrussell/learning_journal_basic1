import pytest

from pyramid import testing


def test_list_view():
    """Test that entries are properly entered into list view."""
    from .views import list_view
    request = testing.DummyRequest()
    info = list_view(request)
    assert "entries" in info


def test_detail_view():
    """Test that correct entry appears in detail view."""
    request = testing.DummyRequest()
    request.id = 1



@pytest.fixture()
def testapp():
    from learning_journal_basic1 import main
    app = main({})
    from webtest import testapp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'Jinja2, Binary Heap' in response.body


def test_root_contents(testapp):
    """Tests that the contents of the root page contin as many articles as journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.finalAll("article"))

    