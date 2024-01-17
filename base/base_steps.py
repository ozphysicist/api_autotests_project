from base.api_client import BaseApiClient


class BaseSteps(object):
    """Base class for test steps"""
    def __init__(self, client):
        """Constructor"""
        self._client: BaseApiClient = client
