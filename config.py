import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{base_dir}/contact.db'.format(base_dir=BASE_DIR)
    FULLCONTACT_API_KEY = os.environ.get('FULLCONTACT_API_KEY', 'None')


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'v#l70zX7ggfEsW!'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
