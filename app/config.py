import os

class Config:
    '''
    General configuration parent class
    '''

    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
