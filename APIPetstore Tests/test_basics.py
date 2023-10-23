import requests, json


baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '1000'


# test valid response or response is not empty
def test_getPetById_response():
    url = baseURI + petID
    print(url)
    header = {'Content-Type': 'application/json'}
    response = requests.get(url=url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0, "empty response"



# testing response body for "ID" key
def test_getPetById_id():
    url = baseURI + petID
    print(url)
    header = {'Content-Type': 'application/json'}
    response = requests.get(url=url, verify=False, headers=header)
    data = response.json()
    assert data['id'] == 1000


# test adding a new pet to the store
def test_addNewPet():
    url = baseURI
    print(url)
    header = {'Content-Type': 'application/json'}
    payload = {
        "id": 1001,
        "name": "Freddie",
        "status": "available"
    }

    response = requests.post(url= url, params=payload, headers=header, verify=False,)
    data = response.json()
    print(data)
    assert data['id'] == 1001
