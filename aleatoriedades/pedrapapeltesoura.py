

import random

ties = 0


class ai:
    rock = 0
    paper = 0
    scissors = 0

    score = 0

    previous = []

    def update(self, rock, paper, scissors, previous):
        if len(previous) > 3:
            target = previous[0]
            if target == 0:
                rock -= 1
            elif target == 1:
                paper -= 1
            elif target == 2:
                scissors -= 1

            previous.pop(0)
        return rock, paper, scissors, previous


class player:
    score = 0
    previous = []


ai_object = ai()

rock_prob = 3.3
paper_prob = 3.3
scissors_prob = 3.3

for x in range(0, 10):
    if rock_prob > 1:
        rock_prob = 1
    elif rock_prob < 0:
        rock_prob = 0

    if paper_prob > 1:
        paper_prob = 1
    elif paper_prob < 0:
        paper_prob = 0

    if scissors_prob > 1:
        scissors_prob = 1
    elif scissors_prob < 0:
        scissors_prob = 0

    print("Please enter Rock, Paper, or Scissors.")
    user = input('>>> ').lower()

    if user == "rock":
        ai_object.rock += 1
        ai_object.previous.append(0)
        player.previous.append(0)

        rock_prob += 0.5
        paper_prob -= 0.25
        scissors_prob -= 0.25

    elif user == "paper":
        ai_object.paper += 1
        ai_object.previous.append(1)
        player.previous.append(1)

        rock_prob -= 0.25
        paper_prob += 0.5
        scissors_prob -= 0.25
    elif user == "scissors":
        ai_object.scissors += 1
        ai_object.previous.append(2)
        player.previous.append(2)

        rock_prob -= 0.25
        paper_prob -= 0.25
        scissors_prob += 0.5
    else:
        while user != "rock" and user != "paper" and user != "scissors":
            print("\nYou can only enter Rock, Paper, or Scissors.")
            print("Please enter Rock, Paper, or Scissors.")
            user = input(">>> ")

    ai_object.rock, ai_object.paper, ai_object.scissors, ai_object.previous = ai_object.update(ai_object.rock,
                                                                                               ai_object.paper,
                                                                                               ai_object.scissors,
                                                                                               ai_object.previous)

    if rock_prob > paper_prob and rock_prob > scissors_prob:
        output = "Paper"
    elif paper_prob > rock_prob and paper_prob > scissors_prob:
        output = "Scissors"
    elif scissors_prob > rock_prob and scissors_prob > paper_prob:
        output = "Rock"
    else:
        rock = 0
        paper = 0
        scissors = 0
        for i in range(len(ai_object.previous) - 1):
            if ai_object.previous[i] == 0:
                rock += 1
            elif ai_object.previous[i] == 1:
                paper += 1
            elif ai_object.previous[i] == 2:
                scissors += 1

        if rock == 2:
            output = "Paper"
        elif paper == 2:
            output = "Scissors"
        elif scissors == 2:
            output = "Rock"
        else:
            options = ["Rock", "Paper", "Scissors"]
            output = options[random.randint(0, 2)]

    if user == "rock":
        if output == "Paper":
            print("\nAI chooses paper... you lose!")
            ai_object.score += 1
        if output == "Scissors":
            print("\nAI chooses scissors... you win!")
            player.score += 1
        if output == "Rock":
            print("\nAI chooses rock... It's a tie!")
            ties += 1
    if user == "paper":
        if output == "Paper":
            print("\nAI chooses paper... It's a tie!")
            ties += 1
        if output == "Scissors":
            print("\nAI chooses scissors... you lose!")
            ai_object.score += 1
        if output == "Rock":
            print("\nAI chooses rock... you win!")
            player.score += 1
    if user == "scissors":
        if output == "Paper":
            print("\nAI chooses paper... you win!")
            player.score += 1
        if output == "Scissors":
            print("\nAI chooses scissors... It's a tie!")
            ties += 1
        if output == "Rock":
            print("\nAI chooses rock... you lose!")
            ai_object.score += 1

# print(f"{ai_object.previous}\n{rock_prob}, {paper_prob}, {scissors_prob}")

print(f"\nYour score: {player.score}\nAI score: {ai_object.score}\nTies: {ties}")