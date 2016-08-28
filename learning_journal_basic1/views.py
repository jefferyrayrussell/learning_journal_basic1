from pyramid.response import Response
# from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)


# @view_config(route_name="index", renderer="templates/index.html")
def list_view(request):
    imported_text = open(os.path.join(HERE, './templates/index.html')).read()
    return Response(imported_text)


# @view_config(route_name="detail", renderer="templates/detail.html")
def detail_view(request):
    imported_text = open(os.path.join(HERE, './templates/detail.html')).read()
    return Response(imported_text)


# @view_config(route_name="entry", renderer="templates/create.html")
def entry_view(request):
    imported_text = open(os.path.join(HERE, './templates/entry.html')).read()
    return Response(imported_text)


# @view_config(route_name="edit", renderer="templates/edit.html")
def edit_view(request):
    imported_text = open(os.path.join(HERE, './templates/edit.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(list_view, route_name='list_view')
    config.add_view(detail_view, route_name='detail_view')
    config.add_view(entry_view, route_name='entry_view')
    config.add_view(edit_view, route_name='edit_view')
