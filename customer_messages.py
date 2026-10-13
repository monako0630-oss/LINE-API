
import csv
from message_selector import select_message

# 承認したお客様を記録するリスト
approved_customers = []

# LINE送信対象者の一覧を読み込む
with open("target_customers.csv", "r", encoding="utf-8-sig") as file:
    customers = csv.DictReader(file)

    for customer in customers:
        name = customer["name"]
        days = int(customer["days"])

        # 経過日数に合ったメッセージを選ぶ
        message = select_message(days)

        
        if message is not None:
            print(f"【{name}へのLINE】")
            print(message)

            answer = input("このメッセージを承認しますか？ (y/n): ")

            if answer.lower() == "y":
                print(f"✅ {name}：送信承認（テスト）")

                approved_customers.append({
                    "name": name,
                    "treatment_date": customer["treatment_date"],
                    "days": days,
                    "message": message
                })

            else:
                print(f"❌ {name}：送信見送り")
    
            print("-----")

print(f"✅ 送信承認したお客様：合計{len(approved_customers)}名")

# 承認したお客様をCSVに保存
with open("approved_customers.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "treatment_date", "days", "message"]
    )
    writer.writeheader()
    writer.writerows(approved_customers)

print("承認したお客様の一覧を保存しました！")