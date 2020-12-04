import random 
import statistics

def tries(maxGames, coins):
    values=[]
    games=0
    while(coins>0 and games<=maxGames):
        coins-=1
        games+=1
        values.append([random.randint(0,3),random.randint(0,3),random.randint(0,3)])
        bar=0 
        bell=0 
        lemon=0
        cherry=0
        for k in values[0]:
            if k == 0:
                bar+=1
            elif k==1:
                bell+=1
            elif k==2:
                lemon+=1
            elif k==3:
                cherry+=1 
        if bar == 3:
            coins+=20
        elif bell == 3:
            coins+=15
        elif lemon == 3:
            coins+=5
        elif cherry == 3:
            coins+=3
        elif cherry == 2:
            coins+=2
        elif cherry == 1:
            coins+=1
        values.clear()
    return games

coins=int(input("Please enter the number of coins: "))
repetitions=int(input("Please enter the number of repetitions for the simulation: "))
maxGames=int(input("Please enter the maximum limit of games per player: "))
result=[]
for i in range(repetitions):
  result.append(tries(maxGames,coins))
mean=statistics.mean(result)
median=statistics.median(result)
print('The number of repetitions: ', repetitions)
print('Maximum games per player: ', maxGames)
print('Mean:', mean, '\nMedian:', median)