import json

dataDict = {
    "sampleString": "Test",
    "sampleList": ["good", "bad", "best"],
    "sampleTuple": ("python", "pytest", "automation"),
    "sampleObj": {"platfrom": "Udemy", "Valuable": "true"},
    "sampleIneger": 2500,
    "booleanValue": True,
    "noneValue": None
}

print("Convert py dict to Json")
resultJson = json.dumps(dataDict, sort_keys=True, indent=4)
#print(resultJson)
print(type(resultJson)==str)

# from  json to data
dat_dic = json.loads(resultJson)
print(type(dataDict))


# with open("example.json", 'r') as file:
#
#     data = json.load(file)
#     print(type(data))
#     print(data.keys())
#     print(data['address'])
#
#     for key, value in data.items():
#         print(key, ":", value)

def validateJson(jsonStr):
    try:
        value = json.loads(jsonStr)
        print(value)
    except ValueError as  err:
        return False
    return True

JsonString = """{"name": "dina, "salary": 25000,}"""


isValid = validateJson(jsonStr=JsonString)

print("JSON string is valid?", isValid)