# TODO: Make this compatible with Python 2

import requests as r

def getWttr(where=None, loc=None):
    if where != None:
        url = 'https://wttr.in/{0}'.format(where)
    else:
        url = 'https://wttr.in/'
    
    if loc != None:
        opts = {"lang": loc}
    else:
        opts = {}
    
    resp = r.get(url, params=opts)

    return resp.text
    