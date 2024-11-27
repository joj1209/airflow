import requests

client_id = '4fce18f119a45da31ca3baf5ff214866'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'CKS5u7kmR4B-Vt8wU76RuHDd0UFK2QW9zyL9ol-rrKAEGawprNIP2AAAAAQKPXLqAAABk02OZo_gLMgnBn6ZSw'


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