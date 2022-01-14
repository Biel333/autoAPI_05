import requests
from decouple import config


def request(method, rout, **kwargs):
    url = config('BASE_URL') + rout
    if "authorization" in kwargs:
        token = config('TOKEN')
        kwargs.pop("authorization")
        if "headers" in kwargs:
            kwargs["headers"] = kwargs["headers"] | {"Authorization": F"Bearer {token}"}
        else:
            kwargs["headers"] = {"Authorization": F"Bearer {token}"}
    return requests.request(method=method, url=url, **kwargs)
