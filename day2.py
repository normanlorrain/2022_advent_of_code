from enum import Enum

test="""A Y
B X
C Z"""

ROCK=1
PAPER=2
SCISSORS=3

codeShapes={'A':ROCK,'B':2,'C':3,'X':ROCK,'Y':PAPER,'Z':SCISSORS}
scoreShape={ROCK:1,PAPER:2,SCISSORS:3}






def weWon(they,we):

    rules={(ROCK,PAPER):True,
        (ROCK,SCISSORS):False,
        (PAPER,ROCK):False,
        (PAPER,SCISSORS): True,
        (SCISSORS, PAPER):False,
        (SCISSORS, ROCK): True}
    return rules[(they,we)]

                
def scoreRound(they,we):
    score=we # "The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)"

    if they==we:
        score+= 3 # "3 if the round was a draw"
    elif weWon(they, we):
        score += 6 # "and 6 if you won"
    # else "0 if you lost"
    return score

    

            


scoreTotal=0
f = test.splitlines()
f = open("day2.txt")
for i in f:
    they,we = i.split()
    they=codeShapes[they]
    we=codeShapes[we]
    scoreTotal+= scoreRound(they,we)

print(scoreTotal)



# part two
LOSE = 1
DRAW = 2 
WIN = 3
codeResult = {'X':LOSE,'Y':DRAW,'Z':WIN}

desiredWe={(ROCK,LOSE):SCISSORS,
        (ROCK,DRAW):ROCK,
        (ROCK,WIN):PAPER,
        (PAPER,LOSE):ROCK,
        (PAPER,DRAW): PAPER,
        (PAPER,WIN): SCISSORS,
        (SCISSORS, LOSE):PAPER,
        (SCISSORS, DRAW): SCISSORS,
        (SCISSORS, WIN): ROCK}
scoreTotal=0
f = test.splitlines()
f = open("day2.txt")
for i in f:
    they,result = i.split()
    they=codeShapes[they]
    result = codeResult[result]
    we=desiredWe[(they,result)]
    scoreTotal+= scoreRound(they,we)

print(scoreTotal)