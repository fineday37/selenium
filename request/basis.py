import json

import requests


def reCSV(method, url, data, **kwargs):
    s = requests.session()
    if method == "get":

        res = s.request(method=method, url=url, params=data, **kwargs)
        return res
    else:
        #data = json.dumps(data)
        res = s.request(method=method, url=url, data=data, **kwargs)
        return res
