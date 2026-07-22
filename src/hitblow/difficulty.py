# 難易度に関する処理をまとめる

def select_difficulty():
    """難易度選択（digits, mode を返す）"""
    while True:
        level = input("難易度を選択 (easy / normal / hard) > ").strip().lower()
        if level == "easy":
            return 3, "easy"
        elif level == "normal":
            return 3, "normal"
        elif level == "hard":
            return 5, "hard"
        else:
            print("easy / normal / hard のどれかを入力してね")


def hint(secret):
    """ヒント（最初の1桁を教える）"""
    return f'ヒント：最初の1ケタ "{secret[0]}"'