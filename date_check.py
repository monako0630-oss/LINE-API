
from datetime import datetime, date

# 施術日を入力する
treatment_date = input("施術日を入力してください（例：2026-10-10）：")

# 入力した文字を日付に変換
try:
    treatment_date = datetime.strptime(
        treatment_date, "%Y-%m-%d"
    ).date()
except ValueError:
    print("日付は2026-10-10の形式で入力してください")
    exit()

# 今日の日付を自動取得
today = date.today()

# 施術日から何日経過したか計算
days = (today - treatment_date).days

print(f"施術から{days}日経過しています")

# アフターケアのタイミングを判定
if days in [0, 3, 30]:
    print("LINEアフターケア案内の対象日です！")
elif days < 0:
    print("まだ施術日前です")
else:
    print("今日はLINE案内の対象日ではありません")
