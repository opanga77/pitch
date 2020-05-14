import os

class Config:
    SECRET_KEY = '57916m8bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    


    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'andersoking77@gmail.com'
    MAIL_PASSWORD = 'matarara'
    SUBJECT_PREFIX = 'One Minute Pitch!'
    SENDER_EMAIL = 'andersoking77@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
