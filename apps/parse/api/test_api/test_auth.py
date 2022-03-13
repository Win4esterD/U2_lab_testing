import requests
import pytest

def test_sign_in():
    response = requests.post('http://127.0.0.1:8000/api/auth/sign-in/', data={"username": "admin", "password": "admin"})
    assert response.status_code == 200 and response.json()['username'] == 'admin'

def test_sign_in_1():
    response = requests.post('http://127.0.0.1:8000/api/auth/sign-in/', data={"username": "wrongname", "password": "wrongpass"})
    assert response.status_code == 401 and response.json()["detail"] == 'No active account found with the given credentials'


def test_sign_out():
    response = requests.get('http://127.0.0.1:8000/api/auth/sign-out/')
    assert response.status_code == 200

def test_sign_up():
    response = requests.post('http://127.0.0.1:8000/api/auth/sign-up/', data={"username": "string", "password": "string"})
    assert response.status_code == 400 or response.status_code == 201


