import random as rd

anser = rd.randint(1,100)
isCorrect = False
times = 0
lbound = 1
hbound = 100
while isCorrect == False:
  print('請於',lbound,'至',hbound,'間猜一個數字')
  
  isGuessOK = False
  while isGuessOK == False:
        try:
            guess = int(input('猜一個數字'))
            if guess >= lbound and guess <= hbound:
                isGuessOK = True
                guess = int(guess)
            else:
                print('輸入的數字不在', lbound, '及', hbound,'之間，請再輸入一次')
        except Exception as e:
            print(e)

  isCorrect = guess == anser
  if isCorrect:
    print('恭喜您，答對了')
  else:
    if guess < anser:
      lbound = guess
    else:
      hbound = guess

