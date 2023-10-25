from utils.apiUtils import post_api_data, get_api_data
import json
from utils.myconfigparser import getFlaskBaseUrl


# loginJsonFile = 'loginValid.json'
baseURI = getFlaskBaseUrl()
# loginURLPath = 'login'
usersUrlPath = 'users'


# @pytest.fixture
# def get_token():
#     loginURL = baseURI + loginURLPath
#     payload = getJsonFromFile(loginJsonFile)
#     resp = post_api_data(loginURL, payload)
#     print(resp.json()['token'])
#
#     token = resp.json()['token']
#
#     yield token

#test get users with fixtures
def test_getUsers(get_token):
    token = get_token
    usersURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = get_api_data(usersURL, headers)
    print(json.dumps(resp_users.json(), indent=4))

    assert resp_users.json()['users'][0]['email']
