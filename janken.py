import player_j as p
import computer as c
import janken_judhe as jj

def janken_main():
    for i in range(1,3):
        print('-----ラウンド${i}-----')
        p.pon()
        c.pon()
        jj.judge()
    
    print(f'【最終結果】\nあなた：{p_cnt}勝\nコンピューター：{c_cnt}勝')
    if p_cnt > c_cnt:
        print('あなたの総合勝利です！')
    else:
        print('コンピューターの総合勝利です！')

if __name__ == '__main__':
    janken_main()