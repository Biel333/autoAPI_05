import requests
from decouple import config


def request(method, route, **kwargs):
    url = config('BASE_URL') + route
    if "authorization" in kwargs and kwargs["authorization"]:
        token = config('ACCESS_TOKEN_AUTH')
        kwargs.pop("authorization")
        if "headers" in kwargs:
            kwargs["headers"] = kwargs["headers"] | {"Authorization": F"Bearer {token}"}
        else:
            kwargs["headers"] = {"Authorization": F"Bearer {token}"}
    elif "authorization" in kwargs and kwargs["authorization"]==False:
        token1 = config('ACCESS_TOKEN_NOT_AUTH')
        kwargs.pop("authorization")
        if "headers" in kwargs:
            kwargs["headers"] = kwargs["headers"] | {"Authorization": F"Bearer {token1}"}
        else:
            kwargs["headers"] = {"Authorization": F"Bearer {token1}"}
    return requests.request(method=method, url=url, **kwargs)
