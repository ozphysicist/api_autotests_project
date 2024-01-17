from enum import Enum


class ResponseCodes(Enum):
    OK = 200
    BAD_REQUEST = 400


class ErrorMessages(Enum):
    INVALID_LOCALE = 'Invalid locale argument'
    BAD_USER_AGENT = 'Bad User-Agent header'
    MORE_THAN = "you can't look up more than 5000 items in the list"


class UserAgents(Enum):
    HH_USER_AGENT = "MyApp/1.0 (my-app-feedback@example.com)"
