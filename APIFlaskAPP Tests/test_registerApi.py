from utils.apiUtils import post_api_data
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskBaseUrl


baseURI = getFlaskBaseUrl()
urlPath = 'register'
registerjsonFile = 'registerApiValid.json'

# testing tegister API with a body from file
def test_registerAPI():
    url = baseURI + urlPath
    payload = getJsonFromFile(registerjsonFile)
    resp = post_api_data(url=url, body=payload)
    print(resp.json())
    assert resp.status_code == 201