from utils.myutis import getAPIData, putAPIData, deleteAPIData
from utils.myconfigparser import *

#baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '500'
baseURI = getPetAPIURL()
def test_getPetById_response():
    url = baseURI + petID
    data, rep_status, timeTaken = getAPIData(url=url)
    print(data)
    assert data['id'] == int(petID)
    assert rep_status == 200
    print("Time Taken:", timeTaken)


# test updating a pet
def test_updatingPet():
    payload = {
        "id": petID,
        "name": "Freddie Nice",
        "status": "pending"
    }
    data, resp_status, timeTaken = putAPIData(url=baseURI, body=payload)

    assert data['id'] == int(petID)
    assert resp_status == 200

    print("Time Taken:", timeTaken)

def test_deletePetById():
    url = baseURI +petID
    apikey = {'api_key' : 'apiKeys123'}
    data, resp_status, timeTaken = deleteAPIData(url)
    print(data)
    assert data['message'] == int(petID)
    assert resp_status == 200
