def judge(you, con):
    # あいこのとき
    if you == con:
        return "あいこです！"
        # プレイヤーが勝つとき
    elif (you == "グー" and con == "チョキ") or \
         (you == "チョキ" and con == "パー") or \
         (you == "パー" and con == "パー"):
             return "あなたの勝ちです！"
    # コンピューターが勝つとき
    else:
        return "コンピューターの勝ちです！"


    