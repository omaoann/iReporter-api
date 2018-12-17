import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = "dbname='ireporter' host='localhost' \
     port='5432' user='postgres' password='naivasha_234'"

class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = "dbname='ireporter_test' host='localhost' \
     port='5432' user='postgres' password='naivasha_234'"    

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    DATABASE_URL = "postgres://mcrmuvfwihukqd:af70c0e3ef1336184829959a903a2fa832f226075bf8631713966ebc9a4e51ac@ec2-54-227-249-201.compute-1.amazonaws.com:5432/d80ka6ct2g6ree"


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}