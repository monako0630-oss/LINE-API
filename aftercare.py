
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

# LINEの設定を読み込む
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
user_id = os.getenv("LINE_USER_ID")

if not channel_access_token or not user_id:
    raise ValueError(".envの設定を確認してください")

# 施術からの日数に合わせたメッセージ
MESSAGES = {
    0: """【アートメイク施術当日】
本日はご来院ありがとうございました。
施術部位を強くこすらず、清潔に保ってください。""",

    3: """【アートメイク施術3日後】
施術後の経過はいかがでしょうか？
かさぶたは無理にはがさず、当院からご案内したケアを続けてください。""",

    30: """【アートメイク施術30日後】
施術から1か月が経過しました。
色味や仕上がりについて気になることがあれば、お気軽にご相談ください。"""
}

# 送信する日数を指定する
if len(sys.argv) != 2:
    print("使い方: python aftercare.py 0")
    sys.exit(1)

try:
    days = int(sys.argv[1])
except ValueError:
    print("日数は 0、3、30 のいずれかを入力してください")
    sys.exit(1)

if days not in MESSAGES:
    print("対応している日数は 0、3、30 です")
    sys.exit(1)

# 自分のLINEへ送信する
url = "https://api.line.me/v2/bot/message/push"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {channel_access_token}",
}

data = {
    "to": user_id,
    "messages": [
        {"type": "text", "text": MESSAGES[days]}
    ],
}

response = requests.post(url, headers=headers, json=data, timeout=15)

if response.status_code == 200:
    print(f"施術から{days}日後の案内を送信しました")
else:
    print(f"送信失敗: {response.status_code}")
    print(response.text)
