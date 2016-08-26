def includeme(config):
    config.add_static_view('static', 'static', chache_max_age=3600)
    config.add_route('home', ' / ')
