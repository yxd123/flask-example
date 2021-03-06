#!/usr/bin/env python
# encoding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "testkey123#125@@!K"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/test?charset=utf8"


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/test?charset=utf8"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}

