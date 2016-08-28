from pyramid.config import Configurator


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.add_static_view(name='static', path='learning_journal_basic1:static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
