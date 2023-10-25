from utils.apiUtils import get_api_data
from utils.myconfigparser import getFlaskBaseUrl

baseURI = getFlaskBaseUrl()
urlPath = 'allusercount'


# testing api call user count for status 200
def test_getALLUserCountStatus200():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = get_api_data(url, headers)
    assert resp.status_code == 200


# testing api call user count for status 406
def test_getALLUserCountStatusCode406():
    url = baseURI + urlPath
    resp = get_api_data(url)
    assert resp.status_code == 406


def test_getALLUserCountBody():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = get_api_data(url, headers)
    data = resp.json()
    print(data)
    assert data['count'] == 4
    assert data['status']
    assert data['status']['message'] == 'success'


def test_getALLUserCountTimeTaken():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = get_api_data(url, headers)
    resp_time = resp.elapsed.total_seconds()
    print(resp_time)
    assert resp_time < 1
