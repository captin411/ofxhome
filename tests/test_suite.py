import sys, os
sys.path.append('..')
from ofxhome import OFXHome, Institution, InstitutionList
import unittest
import datetime

class InstitutionTestCase(unittest.TestCase):
    def testGoodParse(self):
        xml = testfile('scottrade.xml').read()
        i = Institution(xml)
        self.assertEquals(i.id,'623')
        self.assertEquals(i.name,'Scottrade, Inc.')
        self.assertEquals(i.fid,'777')
        self.assertEquals(i.org,'Scottrade')
        self.assertEquals(i.brokerid,'www.scottrade.com')
        self.assertEquals(i.url,'https://ofxstl.scottsave.com')
        self.assertEquals(i.ofxfail,'0')
        self.assertEquals(i.sslfail,'4')
        self.assertEquals(i.lastofxvalidation,datetime.datetime(2012,8,13,22,28,10))
        self.assertEquals(i.lastsslvalidation,datetime.datetime(2011,9,28,22,22,22))
        self.assertEquals(i.xml, xml)

def testfile(filename):
    ''' Load a file from the fixtures directory. '''
    path = 'testfiles/' + filename
    if ('tests' in os.listdir('.')):
        path = 'tests/' + path
    return file(path)


if __name__ == '__main__':
    unittest.main()
