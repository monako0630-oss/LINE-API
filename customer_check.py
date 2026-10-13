import csv
from datetime import datetime, date
# LINE送信対象のお客様を保存するリスト
target_customers = []# LINE送信対象のお客様を保存するリスト

# 今日の日付
today = date.today()

# お客様一覧を読み込む
with open("customers.csv", "r", encoding="utf-8-sig") as file:
    customers = csv.DictReader(file)

    target_count = 0
    for customer in customers:
        name = customer["name"]
        treatment_date = datetime.strptime(
            customer["treatment_date"], "%Y-%m-%d"
        ).date()
        line_user_id = customer["line_user_id"]
        # 施術日からの経過日数を計算
        days = (today - treatment_date).days

        if days in [0, 3, 30]:
            print(f"✅ {name}：施術から{days}日 → LINE送信対象")
            target_count += 1
            target_customers.append({
                "name": name,
                "treatment_date": customer["treatment_date"],
                    "days": days,
    "line_user_id": line_user_id
            })
        else:
            print(f"❌ {name}：施術から{days}日 → 対象外")
print("-----")
print("お客様の判定が完了しました！")
print(f"LINE送信対象：合計{target_count}名")  

print("次は送信対象者の一覧表を作成します！")

# LINE送信対象者をCSVに保存
with open("target_customers.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["name", "treatment_date", "days", "line_user_id"])
    writer.writeheader()
    writer.writerows(target_customers)

print("送信対象者の一覧表を保存しました！")
