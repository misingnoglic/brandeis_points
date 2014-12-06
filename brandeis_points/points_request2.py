__author__ = 'arya'
import cookielib
import urllib, urllib2
import secrets

import requests


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
payload["doLogin.x"]=56
payload["doLogin.y"]=15

data = urllib.urlencode(payload)
req = urllib2.Request(authentication_url, data)
resp = urllib2.urlopen(req)
contents = resp.read()
#print contents

s = requests.session()
login_data = payload
s.post('https://login.brandeis.edu/cgi-bin/cosign.cgi', data=login_data)
r = s.get('https://brandeis.netcardmanager.com/student/welcome.php')

print r.content