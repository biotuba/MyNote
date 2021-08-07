# 三門問題、決勝 21 點
import random as rd

win = 0
lose = 0
for i in range(0, 1000000):
    doors = ["羊", "羊"]
    doors.insert(rd.randint(0,2), "車")
    # print(doors)

    # 讓參賽者挑一個門
    plyr = rd.randint(0, 2)
    # print("參賽者選:", plyr)

    del doors[plyr]

    # 主持人開一隻羊
    doors.remove("羊")

    # print("剩下的是:", doors)
    if doors[0] == "車": 
        win += 1
    else:
        lose += 1

print("win:", win, ", lose", lose)

