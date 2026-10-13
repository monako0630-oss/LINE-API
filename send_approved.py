import csv

# 承認したお客様のCSVを読み込む
with open("approved_customers.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    approved_customers = list(reader)

# 読み込んだお客様を表示
for customer in approved_customers:
    print(f"お客様：{customer['name']}")
    print(f"送信予定メッセージ：{customer['message']}")
    print("-----")

print(f"読み込み完了：合計{len(approved_customers)}名")