import io
from django.test import TestCase
import unittest

from django.utils import timezone
from model_mommy import mommy
from rest_framework.test import APIClient

from api.models import MusicalWork
from api.reconcile import get_iswc_index, obj_params_count, perform_each_line


# These are unit tests no db operations are carried out within the test so are faster
class UnitTestCase(unittest.TestCase):

    def test_get_iswc_index(self):
        headers = ('iswc', 'title', 'contributors', )
        idx = get_iswc_index(headers)
        self.assertEqual(idx, 0)

        headers = ('title', '', 'iswc', 'contributors')
        idx = get_iswc_index(headers)
        self.assertEqual(idx, 2)

    def test_obj_params_count(self):
        obj = MusicalWork(source='abc', iswc='xd56uy', item_id=3)
        count = obj_params_count(obj)
        self.assertEqual(count, 3)

        obj = MusicalWork(item_id='')
        count = obj_params_count(obj)
        self.assertEqual(count, 0)

        obj = MusicalWork(source='', iswc='xd56uy', title='something', item_id='', )
        count = obj_params_count(obj)
        self.assertEqual(count, 2)

    def test_perform_each_line_with_existing_db_value(self):
        iswc_db_check = True # to make db value exist
        obj = MusicalWork(source='abc', contributors='jpt', iswc='axbycz')
        key_item, batch = 'axbycz', 'rtyuxv'
        headers = ('iswc', 'source', 'contributors', 'id', ),
        created_on = timezone.now()
        values = ['axbycz', '', '', 4]
        rows = {'axbycz': obj}
        ret = perform_each_line(key_item, iswc_db_check, headers, batch, created_on, values, rows)
        self.assertIsNone(ret)

    def test_perform_each_line_with_existing_row_value(self):
        obj = MusicalWork(source='abc', contributors='jpt', iswc='axbycz')
        key_item, batch = 'axbycz', 'rtyuxv'
        iswc_db_check = True
        headers = ('iswc', 'source', 'contributors', 'id', ),
        created_on = timezone.now()
        values = ['axbycz', '', '', 4]
        rows = {'axbycz': obj} # to make row value exist for that iswc
        ret = perform_each_line(key_item, iswc_db_check, headers, batch, created_on, values, rows)
        self.assertIsNone(ret)

    def test_perform_each_line_with_no_row_no_db(self):
        key_item, batch = 'axbycz', 'rtyuxv'
        iswc_db_check = False
        headers = ('iswc', 'source', 'contributors', 'id', )
        created_on = timezone.now()
        values = ['axbycz', '', '', 4]
        rows = {}
        ret = perform_each_line(key_item, iswc_db_check, headers, batch, created_on, values, rows)
        self.assertEqual(type(ret), MusicalWork)
        self.assertEqual(ret.iswc, 'axbycz')
        self.assertEqual(ret.contributors, '')
        self.assertEqual(ret.item_id, 4)

    def test_perform_each_line_with_less_value_and_previous_row(self):
        obj = MusicalWork(source='abc', contributors='jpt', iswc='axbycz', title='some title')
        key_item, batch = 'axbycz', 'rtyuxv'
        iswc_db_check = False
        headers = ('iswc', 'source', 'contributors', 'id', )
        created_on = timezone.now()
        values = ['axbycz', '', 'shyam', '4']
        rows = {'axbycz': obj}
        ret = perform_each_line(key_item, iswc_db_check, headers, batch, created_on, values, rows)
        self.assertEqual(type(ret), MusicalWork)
        self.assertEqual(ret.iswc, 'axbycz')
        self.assertEqual(ret.contributors, 'jpt')
        self.assertEqual(ret.item_id, None)

    def test_perform_each_line_with_no_previous_value(self):
        key_item, batch = 'axbycz', 'rtyuxv'
        iswc_db_check = False
        headers = ('iswc', 'source', 'contributors', 'id', )
        created_on = timezone.now()
        values = ['axbycz', '', 'shyam', 4]
        rows = {}
        ret = perform_each_line(key_item, iswc_db_check, headers, batch, created_on, values, rows)
        self.assertEqual(type(ret), MusicalWork)
        self.assertEqual(ret.iswc, 'axbycz')
        self.assertEqual(ret.contributors, 'shyam')
        self.assertEqual(ret.item_id, 4)
        self.assertEqual(ret.source, '')


# functional tests, these test cases are carried out with db operations and are slower than unit test
class APITestCase(TestCase):
    client = APIClient()

    def test_get_api(self):
        mommy.make(MusicalWork, _quantity=5)
        resp = self.client.get('/work-single/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('count'), 5)

    def test_download_api(self):
        resp = self.client.get('/work-single/?download=download')
        self.assertEqual(resp.status_code, 200)
