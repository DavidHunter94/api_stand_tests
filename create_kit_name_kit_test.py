from data import kit_body_1, kit_body_2, kit_body_3, kit_body_4, kit_body_5, kit_body_6, kit_body_7, kit_body_8, \
    kit_body_9
from sender_stand_request import new_kit


def test_kit_body_1():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_1, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body_1['name']

def test_kit_body_2():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_2, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body_2['name']

def test_kit_body_3():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_3, auth_token)
    assert response.status_code == 400

def test_kit_body_4():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_4, auth_token)
    assert response.status_code == 400

def test_kit_body_5():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_5, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body_5['name']

def test_kit_body_6():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_6, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body_6['name']

def test_kit_body_7():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_7, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body_7['name']

def test_kit_body_8():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_8, auth_token)
    assert response.status_code == 400

def test_kit_body_9():
    auth_token = "your_auth_token"
    response = new_kit(kit_body_9, auth_token)
    assert response.status_code == 400
