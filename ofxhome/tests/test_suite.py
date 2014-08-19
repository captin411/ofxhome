import sys, os, os.path
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

    def testOptionalBroker(self):
        xml = testfile('jpmorgan.xml').read()
        i = Institution(xml)
        self.assertEquals(i.id,'435')
        self.assertEquals(i.name,'JPMorgan Chase Bank')
        self.assertEquals(i.fid,'1601')
        self.assertEquals(i.org,'Chase Bank')
        self.assertEquals(i.brokerid,'')
        self.assertEquals(i.url,'https://www.oasis.cfree.com/1601.ofxgp')
        self.assertEquals(i.ofxfail,'0')
        self.assertEquals(i.sslfail,'0')
        self.assertEquals(i.lastofxvalidation,datetime.datetime(2014,8,17,22,23,35))
        self.assertEquals(i.lastsslvalidation,datetime.datetime(2014,8,17,22,23,34))
        self.assertEquals(i.xml, xml)

    def testFromFile(self):
        i = Institution.from_file( testfile_name('scottrade.xml') )
        self.assertEquals(i.id,'623')
        self.assertEquals(i['id'],'623')

    def testDictKeys(self):
        xml = testfile('scottrade.xml').read()
        i = Institution(xml)
        self.assertEquals(i['id'],'623')
        self.assertEquals(i['name'],'Scottrade, Inc.')

        i['id'] = '123'
        self.assertEquals(i['id'],'123')

    def testBadParse(self):
        xml = testfile('badxml_bank.xml').read()
        try:
            l = Institution(xml)
            self.assertFalse(0)
        except Exception:
            self.assertTrue(1)

class InstitutionListTestCase(unittest.TestCase):

    def testFromFile(self):
        l = InstitutionList.from_file( testfile_name('search_america.xml') )
        self.assertEquals(len(l),15)

    def testGoodResult(self):
        xml = testfile('search_america.xml').read()
        l = InstitutionList(xml)
        self.assertEquals(len(l),15)
        self.assertEquals(l.xml,xml)
        self.assertEquals(l[0]['id'],'533')
        self.assertEquals(l[0]['name'],'America First Credit Union')

    def testResultWithPHPError(self):
        xml = testfile('search_noexist.xml').read()
        l = InstitutionList(xml)
        self.assertEquals(len(l),0)
        self.assertEquals(l.xml,xml)

    def testIterator(self):
        count = 0
        xml = testfile('search_america.xml').read()
        l = InstitutionList(xml)
        for i in l:
            count += 1
        self.assertEquals(count,15)

    def testBadXML(self):
        xml = testfile('badxml_search.xml').read()
        try:
            l = InstitutionList(xml)
            self.assertFalse(0)
        except Exception:
            self.assertTrue(1)

def testfile_name(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(base_path,'testfiles',filename)
    if ('tests' in os.listdir('.')):
        path = os.path.join('tests',path)
    return path

def testfile(filename):
    return file(testfile_name(filename))


if __name__ == '__main__':
    unittest.main()
