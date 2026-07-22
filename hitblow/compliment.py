# 試行回数に応じたお祝いメッセージ

def compliment(tries):
    """
    試行回数が少ないときに特別メッセージを返す
    条件は自由に調整OK
    """
    if tries <= 5:
        return f"{tries}回で正解！！素晴らしい！！"
    elif tries <= 10:
        return f"{tries}回で正解！なかなか良いね！"
    else:
        return None