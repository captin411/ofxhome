ofxhome
=========

This is a REST client for the web services provided at ofxhome.com

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
" { name: 'USAA FSB', id: '24234234234' }
" { name: 'USAA Brokerage Services', id: '6564724124' }
for item in s:
    print item.id _ item.name
    bank = OFXHome.lookup(item.id)
    print bank.name _ bank.fid _ bank.url
