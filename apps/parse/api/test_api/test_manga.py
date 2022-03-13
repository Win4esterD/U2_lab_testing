import requests
import pytest
from .manga_title import title

def test_manga_search():
    for i in title:
        response = requests.get('http://127.0.0.1:8000/api/manga?title=' + i + '/')
        assert response.status_code == 200


def test_manga_id():
    for i in range(1, 969):
        response = requests.get('http://127.0.0.1:8000/api/manga/' + str(i))
        assert response.status_code == 200

def test_manga_chapters():
    for i in range(1, 969):
        response = requests.get('http://127.0.0.1:8000/api/manga/' + str(i) + '/chapters')
        assert response.status_code == 200

