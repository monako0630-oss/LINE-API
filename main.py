import os

import requests
from dotenv import load_dotenv

load_dotenv()

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
user_id = os.getenv("LINE_USER_ID")

if not channel_access_token:
    raise ValueError(".env に LINE_CHANNEL_ACCESS_TOKEN を設定してください")

if not user_id:
    raise ValueError(".env に LINE_USER_ID を設定してください")

url = "https://api.line.me/v2/bot/message/push"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {channel_access_token}",
}

data = {
    "to": user_id,
    "messages": [
        {
            "type": "text",
            "text": "LINE Messaging APIのテストメッセージです。",
        }
    ],
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("メッセージを送信しました")
else:
    print(f"送信に失敗しました: {response.status_code}")
    print(response.text)