from pyramid.config import Configurator


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include('.views')
    config.scan()
    return config.make_wsgi_app()
