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
print(resultJson)
print(type(resultJson)==str)
