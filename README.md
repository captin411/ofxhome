ofxhome
=========

This is a REST client for the web services provided at ofxhome.com

ofxhome.com provides a way to discover the Open Financial Exchange (OFX) URL's and financial institution ID's for banks and other financial institutions.

ofxhome is a sort of "DNS" for financial institution OFX URI's.

This client by itself is not all that useful unless you are coupling it with software that needs this lookup capability.

other modules
=============

ofxclient - a python API that downloads transactions from banks

example
=======

from ofxhome import OFXHome

s = OFXHome.search("USAA")
" 's' contains a list that has entries like so:
" { name: 'USAA FSB', id: '24234234234' }
" { name: 'USAA Brokerage Services', id: '6564724124' }
for b in s:
    bank = OFXHome.lookup(b['id'])
    " 'bank.dict()' contains a list that has entries like so
    " {
    "    'id': '483',
    "    'name': 'USAA Federal Savings Bank',
    "    'fid': '24591',
    "    'org': 'USAA',
    "    'url': 'https://service2.usaa.com/ofx/OFXServlet',
    "    'brokerid': '',
    "    'ofxfail': 0,
    "    'sslfail': 0,
    "    'lastofxvalidation': datetime(..)
    "    'lastsslvalidation': datetime(..)
    " }
