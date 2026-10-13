
# 施術後の日数に合わせてメッセージを選ぶ
def select_message(days):
    if days == 0:
        return "本日はご来院ありがとうございました！施術部位を清潔に保ってください。"

    elif days == 3:
        return "施術から3日が経過しました。お肌の状態はいかがでしょうか？"

    elif days == 30:
        return "施術から30日が経過しました。定着具合はいかがでしょうか？"

    else:
        return None

# メッセージ選択のテスト


if __name__ == "__main__":
    for days in [0, 3, 30, 7]:
        message = select_message(days)

        print(f"施術から{days}日後")
        print(message)
        print("-----")

