__author__ = 'arya'
import cookielib
import urllib, urllib2
import secrets

import requests
from random import randrange
def get_html(username,password):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'BrandeisPoints')]
    urllib2.install_opener(opener)
    authentication_url = 'https://login.brandeis.edu/cgi-bin/cosign.cgi'
    payload = {}
    payload['required']="BRANDEIS.EDU,ldapauth"
    payload['ref']="https://apps.brandeis.edu//offsitesso/cbord"
    payload['service']="cosign-OffsiteSSO-apps-prod"
    payload["login"]=secrets.brandeis_user
    payload["password"]=secrets.brandeis_pass
    payload["doLogin.x"]=randrange(1,99)
    payload["doLogin.y"]=randrange(1,99)

    s = requests.session()
    login_data = payload
    s.get('https://login.brandeis.edu/cgi-bin/cosign.cgi')
    s.post('https://login.brandeis.edu/cgi-bin/cosign.cgi', data=login_data)
    r = s.get('https://brandeis.netcardmanager.com/student/welcome.php', verify=False)

    return r.content