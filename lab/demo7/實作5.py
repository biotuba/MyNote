from random import randint


is_win = False
times = 0
result = [0,0,0,0,0,0,0,0]
while is_win == False:
    times += 1
    lottery_win = set() # 產生空的 set
    while len(lottery_win) < 7:
        n = randint(1,48)
        lottery_win.add(n)
    # print('中獎號碼:',lottery_win)
    
    lottery = set() # 產生空的 set
    while len(lottery) < 7:
        n = randint(1,48)
        lottery.add(n)
    # print('我買的:',lottery)

    total = 0
    for n in lottery:
        if n in lottery_win:
            total += 1

    result[total] += 1
    is_win = total == 7
    if times % 10000 == 0:
        print(times,result)


print(times)