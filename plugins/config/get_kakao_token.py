import requests

client_id = '724c28ce911accf6ec9d2cb0fa5e9898'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'puqBVbBHMySboy4YhqgHDuvYU_ZWH33QtDAdLtAHPYwyFZrUqUjgMAAAAAQKPXQRAAABlRvM9SSUJG13ldIf8A'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)
print('------')
print(data)