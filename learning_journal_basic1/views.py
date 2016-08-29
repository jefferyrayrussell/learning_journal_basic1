"""Views controller for Pyramid Learning Journal Application."""

from pyramid.view import view_config

ENTRIES = [
    {'title': ' Pyramid, Herokue, DeQue', 'creation_date': '08.22.16', 'id': 1, 'body': 'Today I learned about Pyramid and Heroku.  Zack and I worked on the DeQue data structure.  The best learning of the day was the discussion around testing in code review.  I think one is always a little more attentive when it is your code being reviewed!  The conversation around testing was very helpful.  My take aways were:  think carefully about what you are testing; test not for just positive results and what is expected; test a variety of different types of parameters:  None, long list, 1 item, empty list; tests should be numerous and well thought out.'},
    {'title': ' Jinja2, Binary Heap', 'creation_date': '08.23.16', 'id': 2, 'body': 'Today I learned about Pyramid Templates and Front-end Testing.  Zack and I worked on the new  data structure.   We spent some time with Will and another team focusing on testing.  We both feel that we need to get much more proficient in this area.  I need how to better use fixtures and the other resources available.  The progress on the learning journal is coming very slowly. I am afraid much of it is going to be left for the weekend.   I was pleased to have the project – election app - I pitched chosen by three other classmates.  It will be great to work with Jeff, Justin, and Crystal.'},
    {'title': ' Alchemy, Priority Queue', 'creation_date': '08.24.16', 'id': 3, 'body': 'Today I learned about the Priority Queue data structure and the Alchemy Scaffolding.   Each day this week I feel like I am taking one step forward and two steps back in terms of keeping up with assignments.  I am learning, but the pace is brutal.  Thankfully the weekend is near and hopefully I can catch up.  Zack and I continued working on the binary heap and focused on testing. I am really looking forward to project week.'},
    {'title': ' PostgreSQL, Graph', 'creation_date': '08.25.16', 'id': 3, 'body': 'Today I learned about Graph Data Structures and PostgreSQL and environment variables in Python. Zach and I got a good start on the Priority Queue assignment and Jeff and I worked on Step1 of the Learning Journal assignment. It was a good day; two steps forward and only two and a half steps back.'},
    {'title': ' Career, Catch Up', 'creation_date': '08.26.16', 'id': 3, 'body': 'Today I was a catch up Friday.  Zach and I worked on the graph data structure.  We were methodical in sketching, pseudo-code, testing, and writing our functions.  It was valuable time spent.  So also was the morning professional development session.  There was a mix of new information and timely reminders about strategies for pitch, profile statement, and tech resumes.'},
]


@view_config(route_name='home', renderer='templates/list.jinja2')
def list_view(request):
    """Return the Index page for a list view in the LJ."""
    return {'entries': ENTRIES}


@view_config(route_name='detail_view', renderer='templates/detail.jinja2')
def detail_view(request):
    """Return detail page to view a single article in the LJ."""
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry


@view_config(route_name='entry_view', renderer='templates/entry.jinja2')
def entry_view(request):
    """Return entry page to create a new article in the LJ."""
    return {'entries': ENTRIES}


@view_config(route_name='edit_view', renderer='templates/edit.jinja2')
def edit_view(request):
    """Return the edit page to edit an article in the LJ."""
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry
