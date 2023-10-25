from utils.fileUtils import  getJsonFromFile
from utils.apiUtils import  post_api_data, get_api_data
from utils.myconfigparser import getFlaskBaseUrl

loginJsonFile = 'loginValid.json'
baseURI = getFlaskBaseUrl()
loginURLPath = 'login'
usersUrlPath = 'users'

# demo test with token

def test_getUsersDemo():
    # 1. login with an existing user
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = post_api_data(loginURL, payload)
    print(resp.json()['token'])
    token = resp.json()['token']

    #2 Call api data
    usersURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = get_api_data(usersURL, headers)
    print(resp.json())




