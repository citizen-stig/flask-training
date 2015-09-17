# -*- encoding: utf-8 -*-
import os
from sqlalchemy import create_engine


class ProductionConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'postgres://flask:flask@localhost:5432/flask'


class TestingConfig(object):
    TESTING = True

    SHORT_DATABASE_URI = 'postgres://flask:flask@localhost:5432'
    TEST_DB_NAME = 'test_flask'
    SECRET_KEY = 'testingkey'
    DATABASE_URI = SHORT_DATABASE_URI + '/' + TEST_DB_NAME

    @staticmethod
    def _create_db(conn):
        conn.connection.connection.set_isolation_level(0)
        conn.execute("create database {0}".format(TestingConfig.TEST_DB_NAME))
        conn.execute('commit')
        conn.connection.connection.set_isolation_level(1)
        conn.close()

    @staticmethod
    def create_test_db():
        engine = create_engine(TestingConfig.SHORT_DATABASE_URI + '/postgres')
        conn = engine.connect()
        conn.execute('commit')
        try:
            TestingConfig._create_db(conn)
        except Exception as exc:
            TestingConfig.drop_test_db()
            TestingConfig._create_db(conn)

    @staticmethod
    def drop_test_db():
        engine = create_engine(TestingConfig.SHORT_DATABASE_URI + '/postgres')
        conn = engine.connect()
        conn.execute('commit')
        try:
            conn.connection.connection.set_isolation_level(0)
            conn.execute("drop database {0}".format(TestingConfig.TEST_DB_NAME))
            conn.connection.connection.set_isolation_level(1)
            conn.execute('commit')
            conn.close()
        except Exception as exc:
            pass

PREFERRED_SETTINGS = os.getenv('FLASK_SETTINGS')

if PREFERRED_SETTINGS == 'testing':
    EnvironmentConfig = TestingConfig
else:
    EnvironmentConfig = ProductionConfig
