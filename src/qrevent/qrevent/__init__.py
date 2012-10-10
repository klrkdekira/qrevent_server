from pyramid.config import Configurator
from qrevent import models

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    db = models.DBConnect(**settings)
    db.connect()

    config = Configurator(settings=settings)
    config.include('qrevent.api.api_include')

    return config.make_wsgi_app()

