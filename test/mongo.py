import logging
import sys
import unittest

from mongoengine import connect, Document, StringField, FileField

from test.utils.fs import mkdir_loop

sys.path.append('/home/john/mine/workplace/py/slark/test/utils/fs')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

connect(db='rtz_2', host='192.168.0.105', port=27017,
        username='root',
        password='123456',
        authentication_source='admin')


class RtzDoc(Document):
    suffix = StringField()
    url = StringField()
    photo = FileField()


class MyTestCase(unittest.TestCase):
    flag = True

    @staticmethod
    def save_to_file(rtz_doc, base_path):
        mkdir_loop(base_path)

        photo = rtz_doc.photo
        with open(base_path + str(rtz_doc.id) + '.' + rtz_doc.suffix, 'wb') as f:
            f.write(photo.read())

    def test_mkdir(self):
        base_path = "/home/john/tmp/images/src/1/2/3/4/5"
        flag = mkdir_loop(base_path)
        self.assertEqual(flag, True)

    def test_search_by_id(self):
        # 从mongo中取出图片
        try:
            rtz_doc = RtzDoc.objects().get(id='5e3e4d641ea3649bc2eb86aa')
            self.save_to_file(rtz_doc, '/home/john/tmp/images/src/tmp/')
        except Exception as e:
            self.flag = False
            log.error(e)
        self.assertEqual(self.flag, True)

    def test_search_some(self):
        try:
            rtz_doc_list = RtzDoc.objects()[5:105]
            for rtz_doc in rtz_doc_list:
                self.save_to_file(rtz_doc, '/home/john/tmp/images/src/tmp/')
        except Exception as e:
            self.flag = False
            log.error(e)
        self.assertEqual(self.flag, True)


if __name__ == '__main__':
    unittest.main()
