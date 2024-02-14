from jose import jwt

from fast_zero.security import create_access_token
from fast_zero.settings import Settings

settings = Settings()


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token


# def test_get_current_user_with_invalid_user(session):
#     token = create_access_token(data={'sub': 'invalid'})

#     try:
#         loop = asyncio.new_event_loop()
#         loop.run_until_complete(get_current_user(session, token))
#     except HTTPException as ex:
#         assert ex.status_code == 401
#     else:
#         assert False, 'Should raise HTTPException'


# def test_get_current_user_with_null_token(session):
#     token = create_access_token(data={})

#     try:
#         loop = asyncio.new_event_loop()
#         loop.run_until_complete(get_current_user(session, token))
#     except HTTPException as ex:
#         assert ex.status_code == 401
#     else:
#         assert False, 'Should raise HTTPException'
