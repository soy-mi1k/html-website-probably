score = 0
name = input("what is your name?")
attempts = 0

question = int(input("What is 1+1?"))

if question != 2:
    while question != 2 and attempts != 2:
        question = int(input("what is 1+1?"))
        attempts = attempts + 1
        if question == 2:
            score = score+1
        else:
            score = score
elif question == 2:
    score = score+1

attempts = 0

while question != 4 and attempts != 2:
    question = int(input("what is 2+2?"))
    attempts = attempts + 1
    if question == 4:
        score = score+1
    else:
        score = score

attempts = 0

while question != 6 and attempts != 3:
    question = int(input("what is 3+3?"))
    attempts = attempts + 1
    if question == 6:
        score = score+1
    else:
        score = score

attempts = 0

while question != 8 and attempts != 3:
    question = int(input("what is 4+4?"))
    attempts = attempts + 1
    if question == 8:
        score = score+1
    else:
        score = score

attempts = 0

while question != 10 and attempts != 3:
    question = int(input("what is 5+5?"))
    attempts = attempts + 1
    if question == 10:
        score = score+1
    else:
        score = score

print(name, "You got,", score)