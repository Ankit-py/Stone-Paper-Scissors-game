import random
p1=0
p2=0
choices = ['rock','paper','scissors']

while True:
    print("\033c")
    roll1 = random.choice(choices)
    roll2 = random.choice(choices)
    print("wins : "+str(p1)+"player 1 : ",roll1)
    print("wins : "+str(p2)+"player 2 : ",roll2)

    if roll1 == 'scissors' and roll2 == 'scissors':
        print("")
        print("scissors + scissors = Tied")
    elif roll1 == 'scissors' and roll2 == 'paper':
        print("")
        print("Player 1 WINS !! scissors cut paper")
        p1 +=1
    elif roll1 == 'scissors' and roll2 == 'rock':
        print("")
        print("player 2 WINS !! rock crushed scissors")
        p2+=1
    if roll1 == 'rock' and roll2 == 'rock':
        print("")
        print("rock + rock = Tied")
    elif roll1 == 'rock' and roll2 == 'scissors':
        print("")
        print("player 1 WINS !! rock crushed scissors")
        p1 +=1
    elif  roll1 == 'rock' and roll2 == 'paper':
        print("")
        print("player 2 WINS !! paper covered rock")
        p2+= 1
    if roll1 == 'paper' and roll2 == 'paper':
        print("")
        print("paper + paper = tied")
    elif roll1 == 'paper' and roll2 == 'rock':
        print("")
        print("player 1 WINS !! paper covered rock")
        p1 +=1
    elif roll1 == 'paper' and roll2 == 'scissors':
        print("")
        print("player 2 WINS !! scissors cut paper")
        p2 += 1
    print("")
    input("Again ? (Y/n)")