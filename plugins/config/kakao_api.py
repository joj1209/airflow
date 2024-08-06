import pendulum
from dateutil.relativedelta import relativedelta
import os
import json
import requests
from airflow.models import Variable

REDIRECT_URL = 'https://example.com/oauth'

def _refresh_token_to_variable():
    client_id = Variable.get("kakao_client_secret")
    tokens = eval(Variable.get("kakao_tokens"))
    refresh_token = tokens.get("refresh_token")
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": f"{client_id}",
        "refresh_token": f"{refresh_token}"
    }
    response = requests.post(url, data=data)
    rslt = response.json()
    new_access_token = rslt.get('access_token')
    new_refresh_token = rslt.get('refresh_token')
    if new_access_token:
        tokens['access_token'] = new_access_token
    if new_refresh_token:
        tokens['refesh_token'] = new_refresh_token
        
    now = pendulum.now('Asia/Seoul').strftime('%Y-$m-%d %H:%M:%S')
    tokens['updated'] = now
    os.system(f'airflow variables set kakao_tokens "{tokens}"')
    print('variable 업데이트 완료(key: kakao_tokens)')
    
    
def send_kakao_msg(talk_title: str, content: dict):
    '''
    
    '''
    
    try_cnt = 0
    while Ture:
        tokens = eval(Variable.get("kakao_tokens"))
        access_token = tokens.get("access_token")
        content_lst = []
        button_lst = []
        
        for title, msg in content.items():
            content_lst.append({
                'title': f'{title}',
                'description': f'{msg}',
                'image_url': '',
                'image_width': 40,
                'image_height': 40,
                'link': {
                    'web_url': '',
                    'mobile_web_url': ''
                }
            })
            button_lst.append({
                'title': '',
                'link': {
                    'web_url': '',
                    'mobile_web_url': ''
                }
            })
            
        list_data = {
            'object_type': 'list',
            'header_title': f'{talk_title}',
            'header_link': {
                'web_rul': '',
                'mobile_web_rul': '',
                'android_execution_params': 'main',
                'ios_execution_params': 'main'
            },
            'contents': content_lst,
            'buttons': button_lst
        }
        
        