import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """docstring for Config"""
    SECRET_KEY = 'asdafdsfasdasd'

#    @staticmethod
#    def init_app(app):
#        pass


class Default_config(Config):
    """docstring for Default_config"""
    DEBUG = True
    DATABASE = {
    'name': 'lagou',
    'engine': 'peewee.MySQLDatabase', 
    'user': 'root', 
    'passwd': 'qwer'
    }


config = {
    "DefultConfigName": Default_config
}
