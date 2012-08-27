ofxhome
=========

REST client for the web service provided by ofxhome.com

ofxhome.com provides a way to discover the Open Financial Exchange (OFX) URL's and financial institution IDs for banks and other financial institutions.

ofxhome is a sort of "DNS" for financial institution OFX URLs and IDs.

This client by itself is not all that useful unless you are coupling it with software that needs this lookup capability.

other modules
=============

ofxclient - a python API that downloads transactions from banks

example
=======

from ofxhome import OFXHome

s = OFXHome.search("USAA")
" 's' contains a list that has entries like so:
" { name: 'USAA Federal Savings Bank', id: '483' }
" { name: 'USAA Investment Mgmt Co', id: '665' }
for item in s:
    print item['id'] _ item['name']
    bank = OFXHome.lookup(item.id)
    print bank.name _ bank.fid _ bank.url _ bank.brokerid # OR
    print bank['name'] _ bank['fid'] _ bank['url'] _ bank['brokerid']
