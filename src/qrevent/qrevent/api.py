"""
call qnack
tweet
surf
"""

from qrevent import models

def api_include(config):
    config.add_route('api.validate', '/api/validate')
    config.add_route('api.submit', '/api/submit')

class API(object):
    def __init__(self, request):
        self.request = request
        self.session = models.DBSession()
        self.check_access()

    def check_access(self):
        pass


    
# {'action':['tweet', 'surf', 'qnack']
#  'verified':True,
#  'issuer':'Issuer'}


# db

# account

# api

# link


# action

# surf -proceed to surf

# qnack - prompt login with qnack

# tweet - if verified different content 

# class API(object):
#     pass

