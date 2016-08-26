from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    imported_text = open(os.path.join(HERE, '/templates/home.html')).read()
    return Response(imported_text)


def detail_view(request):
    imported_text = open(os.path.join(HERE, '/templates/detail.html')).read()
    return Response(imported_text)


def create_view(request):
    imported_text = open(os.path.join(HERE, '/templates/new.html')).read()
    return Response(imported_text)


def update_view(request):
    imported_text = open(os.path.join(HERE, '/templates/edit.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(list_view, route_name='list_view')
    config.add_view(detail_view, route_name='detail_view')
    config.add_view(create_view, route_name='create_view')
    config.add_view(update_view, route_name='update_view')
