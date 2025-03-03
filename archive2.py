import pyfiglet
import time 
from colorama import Fore

# 2nd archive where I developed it even further to allow more players into the game based on the input

players = []


welcome_message = pyfiglet.figlet_format("Welcome to the FizzBuzz Game!", justify="center", width=110)
print(Fore.BLUE + welcome_message)
time.sleep(1.5)
print("Here are the rules:\nNumbers will appear on the screen\nIf the number is divisible by 3 type in 'fizz'\nIf the number is divisible by 5 type in 'buzz'\nIf it is divisble by both type in 'fizzbuzz'\nIf its neither type in the number!\nEnjoy!'")

response = input("are you ready to play? (y): ")

if response == "y":
    pass

print("")
print(">>> Starting game in 3...")
time.sleep(1)
print(">>> 2...")
time.sleep(1)
print(">>> 1...")
time.sleep(1)
print("")


number_of_players = int(input("Enter the amount of players: "))

for i in range(number_of_players):
    names = input(f"Enter name of player: ")
    players.append(names)

game_running = True
winning_player = "nothing"

p1turn = True
p2turn = False
count = 1
index = 0

def check_answer():
    if count % 3 == 0 and count % 5 == 0:
        global correct_answer
        correct_answer = "fizzbuzz"
    elif count % 3 == 0:
        correct_answer = "fizz"
    elif count % 5 == 0:
        correct_answer = "buzz"
    else:
        correct_answer = count 
        

while game_running:
    #print(count)
    for index in range(len(players)):
        while index < len(players):
            print(f"The number is {count}")
            player_ans = input(f"Type in your answer {players[index]}: ")
            check_answer()
            if player_ans.isdigit() and type(correct_answer) is int:
                ans = int(player_ans)
                if ans == correct_answer:
                    print("correct")
                    count += 1
                    break
                else:
                    print("incorrect or you took to long, you are eliminated")
                    players.pop(index)
                    if len(players) <= 1:
                        winning_player = players[0]
                        #print(players)
                        game_running = False
                        break
                    else:
                        break
            elif isinstance(player_ans, str) and type(correct_answer) is str:
                ans = str(player_ans)
                if ans == correct_answer:
                    print("correct")
                    count += 1
                    break
                else:
                    print("incorrect, you are eliminated")
                    players.pop(index)
                    if len(players) <= 1:
                        winning_player = players[0]
                        game_running = False
                        break
                    else:
                        break
            else:
                print("incorrect, you are eliminated")
                players.pop(index)
                winning_player = players[0]
                game_running = False
                break
    index += 1
    
print(f"The winner is {winning_player}")