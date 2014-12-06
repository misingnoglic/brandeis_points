__author__ = 'arya'
import cookielib
import urllib, urllib2
import secrets

import requests
from random import randrange
from BeautifulSoup import BeautifulSoup

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
    r = s.get('https://brandeis.netcardmanager.com/student/welcome.php')
    html_file = r.content
    beginning = '<table class="Data" cellpadding=0 cellspacing=2>'


    table1_start = html_file.find(beginning)
    table1_end = html_file.find('</table>',table1_start)+len("</table>")
    points = r.content[table1_start:table1_end]
    table2_start = html_file.find(beginning,table1_end)
    table2_end = html_file.find('</table>',table2_start)+len("</table>")
    meals = r.content[table2_start:table2_end]

    points_data = {}
    meal_data = {}
    match = [(points,points_data),(meals,meal_data)]

    for html,dict in match:
        soup = BeautifulSoup(html)
        rows = soup.findAll('tr')
        for row in rows:
            cols = row.findAll('td')


            dict[cols[0].text]=cols[1].text

    return [points_data,meal_data]