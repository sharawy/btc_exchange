
class APIIntegrationException(Exception):
    def __init__(self, message='service is not available now , try again later'):
        self.message = message

    def __str__(self):
        return self.message
