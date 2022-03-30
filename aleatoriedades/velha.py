#https://replit.com/@1Tim/TicTacToe?v=1




from os import system, name as OSname

symbols = ["⬛", "⚪", "❌"]
data = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
won = 0


def update():
    system('cls' if OSname == 'nt' else 'clear')
    send = "TIC TAC TOE ʋ1.0\n\nPlayer 1: ⚪\nPlayer 2: ❌\n\nBoard:\n\n"
    i = 0
    for i,item in enumerate(data):
        i += 1
        send = f"{send} {symbols[item]}"
        if i % 3 == 0:
            send = f"{send}\n"
    print(send)
    print("\nThis is how the fields are numbered:\n\n 1️⃣ 2️⃣ 3️⃣\n 4️⃣ 5️⃣ 6️⃣\n 7️⃣ 8️⃣ 9️⃣\n")


def process(turn, field):
    if data[field] == 0:
        data[field] = turn
    else:
        return turn, 0

    if not 0 in data: return turn, 3

    i = 0
    while True:
        if data[i] != turn: break
        i = i + 1
        if i == 3: return turn, turn
    i = 3
    while True:
        if data[i] != turn: break
        i = i + 1
        if i == 6: return turn, turn
    i = 6
    while True:
        if data[i] != turn: break
        i = i + 1
        if i == 9: return turn, turn

    i = 0
    while True:
        if data[i] != turn: break
        i = i + 3
        if i == 9: return turn, turn
    i = 1
    while True:
        if data[i] != turn: break
        i = i + 3
        if i == 10: return turn, turn
    i = 2
    while True:
        if data[i] != turn: break
        i = i + 3
        if i == 11: return turn, turn

    i = 0
    while True:
        if data[i] != turn: break
        i = i + 4
        if i == 12: return turn, turn
    i = 2
    while True:
        if data[i] != turn: break
        i = i + 2
        if i == 8: return turn, turn

    if turn == 1:
        turn = 2
    else:
        turn = 1

    return turn, 0


while True:
    update()

    if won != 0:
        if won == 3:
            print("Draw!")
            break
        else:
            print(f"Player {won} won!")
            break

    if turn == 1:
        print("It's Player 1's turn!\n")
    else:
        print("It's Player 2's turn!\n")
    field = input("Please enter a number between 1 and 9 to select a field:")
    try:
        if 0 < int(field) < 10: turn, won = process(int(turn), int(field) - 1)
    except Exception:
        pass