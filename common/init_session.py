from . import config
from . import get_token


def init_session(username=None,password=None):
    token  = get_token(username,password)
    config.init(token)
    return token