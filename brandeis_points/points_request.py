__author__ = 'arya'
import cookielib
import urllib, urllib2
import secrets
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
data = urllib.urlencode(payload)
req = urllib2.Request(authentication_url, data)
resp = urllib2.urlopen(req)
contents = resp.read()
print contents