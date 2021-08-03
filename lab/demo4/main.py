# 剪刀、石頭、布 小遊戲
import random as rd

plyrA = int(input("請出拳 0: 剪刀、1: 石頭、2: 布"))
plyrB = int(rd.randint(0,2))
punch = ["剪刀", "石頭", "布"]

if plyrA == plyrB:
    print("你出: ", punch[plyrA], ", 電腦出: ", punch[plyrB], ", 平手。")
elif plyrA == (plyrB + 1) % 3:
    print("你出: ", punch[plyrA], ", 電腦出: ", punch[plyrB], ", 你贏。")
else:
    print("你出: ", punch[plyrA], ", 電腦出: ", punch[plyrB], ", 電腦贏。")

