import pytest
from utils.apiUtils import get_api_data
from utils.myconfigparser import getFlaskBaseUrl

baseURI = getFlaskBaseUrl()
urlPtah = 'allusercount'

testData = [
    ('application/json', 200),
    ('application/xml', 406),
    ('application/mixed', 406),
    ('text/html', 200)  # input, output
]
@pytest.mark.parametrize("type, status", testData)
def test_getAllUserCountStatus(type, status):
    url =baseURI + urlPtah
    headers = {'Accept': type}
    resp = get_api_data(url, headers)
    print(resp.status_code)
    assert resp.status_code == status
