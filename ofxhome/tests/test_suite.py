import sys, os, os.path
from ofxhome import OFXHome, Institution, InstitutionList
import unittest
import datetime

class InstitutionTestCase(unittest.TestCase):

    def testGoodParse(self):
        with testfile('scottrade.xml') as f:
            xml = f.read()
        i = Institution(xml)
        self.assertEqual(i.id,'623')
        self.assertEqual(i.name,'Scottrade, Inc.')
        self.assertEqual(i.fid,'777')
        self.assertEqual(i.org,'Scottrade')
        self.assertEqual(i.brokerid,'www.scottrade.com')
        self.assertEqual(i.url,'https://ofxstl.scottsave.com')
        self.assertEqual(i.ofxfail,'0')
        self.assertEqual(i.sslfail,'4')
        self.assertEqual(i.lastofxvalidation,datetime.datetime(2012,8,13,22,28,10))
        self.assertEqual(i.lastsslvalidation,datetime.datetime(2011,9,28,22,22,22))
        self.assertEqual(i.xml, xml)

    def testOptionalBroker(self):
        with testfile('jpmorgan.xml') as f:
            xml = f.read()
        i = Institution(xml)
        self.assertEqual(i.id,'435')
        self.assertEqual(i.name,'JPMorgan Chase Bank')
        self.assertEqual(i.fid,'1601')
        self.assertEqual(i.org,'Chase Bank')
        self.assertEqual(i.brokerid,'')
        self.assertEqual(i.url,'https://www.oasis.cfree.com/1601.ofxgp')
        self.assertEqual(i.ofxfail,'0')
        self.assertEqual(i.sslfail,'0')
        self.assertEqual(i.lastofxvalidation,datetime.datetime(2014,8,17,22,23,35))
        self.assertEqual(i.lastsslvalidation,datetime.datetime(2014,8,17,22,23,34))
        self.assertEqual(i.xml, xml)

    def testFromFile(self):
        i = Institution.from_file( testfile_name('scottrade.xml') )
        self.assertEqual(i.id,'623')
        self.assertEqual(i['id'],'623')

    def testDictKeys(self):
        with testfile('scottrade.xml') as f:
            xml = f.read()
        i = Institution(xml)
        self.assertEqual(i['id'],'623')
        self.assertEqual(i['name'],'Scottrade, Inc.')

        i['id'] = '123'
        self.assertEqual(i['id'],'123')

    def testBadParse(self):
        with testfile('badxml_bank.xml') as f:
            xml = f.read()
        try:
            l = Institution(xml)
            self.assertFalse(0)
        except Exception:
            self.assertTrue(1)

class InstitutionListTestCase(unittest.TestCase):

    def testFromFile(self):
        l = InstitutionList.from_file( testfile_name('search_america.xml') )
        self.assertEqual(len(l),15)

    def testGoodResult(self):
        with testfile('search_america.xml') as f:
            xml = f.read()
        l = InstitutionList(xml)
        self.assertEqual(len(l),15)
        self.assertEqual(l.xml,xml)
        self.assertEqual(l[0]['id'],'533')
        self.assertEqual(l[0]['name'],'America First Credit Union')

    def testResultWithPHPError(self):
        with testfile('search_noexist.xml') as f:
            xml = f.read()
        l = InstitutionList(xml)
        self.assertEqual(len(l),0)
        self.assertEqual(l.xml,xml)

    def testIterator(self):
        count = 0
        with testfile('search_america.xml') as f:
            xml = f.read()
        l = InstitutionList(xml)
        for i in l:
            count += 1
        self.assertEqual(count,15)

    def testBadXML(self):
        with testfile('badxml_search.xml') as f:
            xml = f.read()
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
    return open(testfile_name(filename))


if __name__ == '__main__':
    unittest.main()
