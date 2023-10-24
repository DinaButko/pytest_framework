import requests, json


# get API call and return response data
def getAPIData(url):
    headers = {'Content-Type': 'application/json'}
    print("RequestURL:  ", url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "empty response"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


#  API call to update a pet
def putAPIData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("RequestURL:  ", url)
    print("Body: ", json.dumps(body))
    response = requests.put(url, verify=False, headers=headers, json=body)
    data = response.json()
    assert len(data) > 0, "empty response"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


#  API call to delete a pet
def deleteAPIData(url, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    print("RequestURL:  ", url)
    """value when true if condition else value_when_false. e...g pass=true if marks>50 else fail"""
    #ternary operator. | oprator that we can use to merge two dictionaries
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.delete(url, verify=False, headers=headers)
    print(response )
    print(response.request.headers)
    data = response.json()
    assert len(data) > 0, "empty response"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken
