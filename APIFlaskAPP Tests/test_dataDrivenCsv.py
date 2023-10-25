from utils.fileUtils import get_csv_data_as_dic
from utils.apiUtils import post_api_data
from utils.myconfigparser import getFlaskBaseUrl
from utils.fileUtils import get_csv_data_as_dic

baseURI = getFlaskBaseUrl()
dataFile = 'registerApiData.csv'
urlPath = 'register'


# register data in a database from csv file

def register_data():
    url = baseURI + urlPath
    payload = get_csv_data_as_dic(filename=dataFile)
    response = post_api_data(url=url, body=payload)
    status_code = response.status_code
    assert status_code == 201
