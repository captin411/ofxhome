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

    def testDictKeys(self):
        xml = testfile('scottrade.xml').read()
        i = Institution(xml)
        self.assertEquals(i['id'],'623')
        self.assertEquals(i['name'],'Scottrade, Inc.')

        i['id'] = '123'
        self.assertEquals(i['id'],'123')

    def testBadParse(self):
        xml = testfile('badxml_bank.xml').read()
        with self.assertRaises(Exception):
            i = Institution(xml)

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
        with self.assertRaises(Exception):
            l = InstitutionList(xml)

def testfile_name(filename):
    path = 'testfiles/' + filename
    if ('tests' in os.listdir('.')):
        path = 'tests/' + path
    return path

def testfile(filename):
    return file(testfile_name(filename))


if __name__ == '__main__':
    unittest.main()
