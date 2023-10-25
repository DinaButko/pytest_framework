from utils.fileUtils import  getJsonFromFile
from utils.apiUtils import  post_api_data, get_api_data
from utils.myconfigparser import getFlaskBaseUrl
import pytest
loginJsonFile = 'loginValid.json'
baseURI = getFlaskBaseUrl()
loginURLPath = 'login'
usersUrlPath = 'users'




@pytest.fixture
def get_token():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = post_api_data(loginURL, payload)
    print(resp.json()['token'])

    token = resp.json()['token']

    yield token