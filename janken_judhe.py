def judge():
    p_cnt = 0
    c_cnt = 0
    # あいこのとき
    if hand == c_hand:
        print('あいこです！')
        # プレイヤーが勝つとき
    elif (hand == "グー" and c_hand == "チョキ") or \
         (hand == "チョキ" and c_hand == "パー") or \
         (hand == "パー" and c_hand == "パー"):
             p_cnt += 1
             return "あなたの勝ちです！"
    # コンピューターが勝つとき
    else:
        c_cnt += 1
        return "コンピューターの勝ちです！"
        
    
    