import requests, json

def get_api_data(url, opHeadr=None):
    headers = {'Content-Type': 'application/json'}
    headers =(headers | opHeadr) if isinstance(opHeadr, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print("\nRequestURL:" + url)
    print("request header:", response.request.headers)
    print("response header:", response.headers)
    return response