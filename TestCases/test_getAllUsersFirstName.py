import requests
import json
import jsonpath


def test_All_Users_FirstName():
    url = 'https://reqres.in/api/users?page=2'
    res = requests.get(url)
    assert res.status_code == 206
    json_res = json.loads(res.text)

    for i in range (0,6):
        firstName = jsonpath.jsonpath(json_res, 'data['+str(i)+'].first_name')
        print((firstName[0]))


def test_All_StatusCode():
    url = 'https://reqres.in/api/users?page=2'
    res = requests.get(url)
    assert res.status_code == 200


