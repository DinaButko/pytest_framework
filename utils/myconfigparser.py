import configparser

from pathlib import Path

cfgFile = 'petsqa.ini'
cfgFileDir = 'config'

cfgFileFlaskApp = 'qa.ini'




config = configparser.ConfigParser()
configFlaskApp = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
print(BASE_DIR)
CONFIG_FILE_FLASKAPP = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFileFlaskApp)

config.read(CONFIG_FILE)
configFlaskApp.read(CONFIG_FILE_FLASKAPP)


def getPetAPIURL():
    return (config['pet']['url'])

def getFlaskBaseUrl():
    baseURL = 'http://' + configFlaskApp['flaskapp']['url'] + ":" + configFlaskApp['flaskapp']['port'] + '/api/'
    return baseURL


print(getFlaskBaseUrl())