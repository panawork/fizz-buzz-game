# first archive ever where the game only took place with 2 players

player_one = input("Enter your name: ")
player_two = input("Enter your name: ")
game_running = True

p1turn = True
p2turn = False

while game_running:
    while p1turn:
        player_one_ans = int(input(f"Enter a number {player_one}: "))
        if player_one_ans % 3 == 0:
            print("Fizz!")
            p1turn = False
            p2turn = True
        else:
            p1turn = False
            p2turn = True
    while p2turn:
        player_two_ans = int(input(f"Enter a number {player_two}: "))
        if player_two_ans % 3 == 0:
            print("Fizz!")
            p1turn = True
            p2turn = False
        else:
            p1turn = True
            p2turn = False