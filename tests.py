# -*- encoding: utf-8 -*-
import unittest

from models import db, User
from config import TestingConfig
from demo import app


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestingConfig.create_test_db()
        cls.app = app
        cls.client = cls.app.test_client()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        db.session.begin(subtransactions=True)

    def tearDown(self):
        db.session.rollback()
        db.session.close()
        TestingConfig.drop_test_db()


class UserTestCase(BaseTestCase):

    def test_without_db(self):
        print('Hello')

    def test_with_user_creation(self):
        u = User(first_name="john", last_name="doe", email="john@example.com",
                 password="letmein")
        db.session.add(u)
        db.session.commit()
        response = self.client.get('/')
        print(response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
