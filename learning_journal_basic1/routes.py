"""This is the routes file."""


def includeme(config):
    """Add routes to Pyramid's Configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('entry_view', '/journal/new_entry')
    config.add_route('edit_view', '/journal/edit_view/{id:\d+}')
