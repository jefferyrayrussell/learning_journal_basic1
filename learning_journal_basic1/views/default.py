from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import MyModel
from pyramid.httpexceptions import HTTPFound

ENTRIES = [
    {
        "title": "Day1",
        "id": 1,
        "date": "August 21, 2016",
        "body": "Today I learned about Chevrolet."
    },
    {
        "title": "Day2",
        "id": 2,
        "date": "August 22, 2016",
        "body": "Today I learned about Ford."
    },
    {
        "title": "Day3",
        "id": 3,
        "date": "August 23, 2016",
        "body": "Today I learned about Chrysler."
    },
    {
        "title": "Day4",
        "id": 4,
        "date": "August 24, 2016",
        "body": "Today I learned about Dodge."
    },
]


@view_config(route_name='home', renderer='../templates/list.jinja2')
def home_view(request):
    """Disply a list of all entries in the database on Home Page."""
    try:
        query = request.dbsession.query(MyModel)
        # query = request.dbsession.query.orderby.all(MyModel)
        entries = query.all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {"entries": entries}


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Display details of a particular entry based on id."""
    try:
        query = request.dbsession.query(MyModel)
        entry = query.filter(MyModel.id ==
                             int(request.matchdict['id'])).first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'entry': entry}


@view_config(route_name='entry_view', renderer='../templates/entry.jinja2')
def entry_view(request):
    """Display an empty form on GET."""
    """Create a new entry, a new model, and return to the Home on POST."""
    """Display an error message if inputs title/body are left empty."""
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        if request.POST['title'] != '' or request.POST['body'] != '':
            new_title = request.POST['title']
            new_body = request.POST['body']
            new_date = request.Post['date']
            entry = MyModel(title=new_title, body=new_body, date=new_date)
            request.dbsession.add(entry)
            return HTTPFound(request.route_url('home'))
        else:
            error_msg = "Cannot submit empty entry."
            return {'error_msg': error_msg}


@view_config(route_name='edit_view', renderer='../templates/edit.jinja2')
def edit_view(request):
    """Display details of a single entry on GET."""
    """Edit an existing entry and go to home page on POST."""
    if request.method == "GET":
        return detail_view(request)
    elif request.method == 'POST':
        if request.POST['title'] != '' or request.POST['body'] != '':
            new_title = request.POST['title']
            new_body = request.POST['body']
            new_date = request.Post['date']
            entry = MyModel(title=new_title, body=new_body, date=new_date)
            request.dbsession.add(entry)
            return HTTPFound(request.route_url('home'))
        else:
            error_msg = "Cannot submit empty entry."
            return {'error_msg': error_msg}
        return HTTPFound(request.route_url('home'))


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_jeff_learning_journal_basic1_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
