import datetime
from qrevent import models, modules

def api_include(config):
    # config.include('qrevent.error.api_error_include')
    config.add_route('api.identify', '/api/identify')
    config.add_route('api.action', '/api/action')

    config.add_view(API, attr='validate',
                    route_name='api.identify',
                    renderer='json',
                    accept='application/json')
    
class Origin(object):
    def __init__(self, request):
        self.request = request
        self.session = models.DBSession()
        self.check_access()

    def validate_submission(self, **args):
        p = self.request.params
        for field in args:
            if not p.get(field):
                raise Exception('Mandatory field "%s" is not found.')        

class API(Origin):
    def validate(self):
        p = self.request.params
        qr = p.get('qr')

        analyse = modules.QRAnalyse(qr)
        resp = analyse.response(**self.request.registry.settings)

        return resp
        
    def submit(self):
        return {}


