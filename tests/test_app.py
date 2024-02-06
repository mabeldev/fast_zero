from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_html_deve_retornar_200_e_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == 200
    assert 'Olá Mundo' in response.text
