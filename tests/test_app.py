def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_with_invalid_user(client):
    response = client.post(
        '/token',
        data={'username': 'any', 'password': 'any'},
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect email or password'}
