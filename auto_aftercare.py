import os
import requests
from datetime import datetime, date
from dotenv import load_dotenv

# LINEの設定を読み込む
load_dotenv()

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
user_id = os.getenv("LINE_USER_ID")

if not channel_access_token or not user_id:
    raise ValueError(".envの設定を確認してください")

# 日数ごとのアフターケア案内
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

# 施術日を入力する
treatment_date = input("施術日を入力してください（例：2026-10-07）：")

try:
    treatment_date = datetime.strptime(
        treatment_date, "%Y-%m-%d"
    ).date()
except ValueError:
    print("日付は2026-10-07の形式で入力してください")
    raise SystemExit(1)

# 今日の日付から経過日数を計算
today = date.today()
days = (today - treatment_date).days

print(f"施術から{days}日経過しています")

# 対象日だけLINEへ送信
if days in MESSAGES:
    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }

    data = {
        "to": user_id,
        "messages": [
            {"type": "text", "text": MESSAGES[days]}
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=15
    )

    if response.status_code == 200:
        print("LINEへの送信に成功しました！")
    else:
        print(f"送信失敗：{response.status_code}")
        print(response.text)
else:
    print("今日はアフターケア案内の対象日ではありません")