import pyfiglet
import time 
from colorama import Fore

# first archive where I managed to use object oriented programming with the game

players = []

welcome_message = pyfiglet.figlet_format("Welcome to the FizzBuzz Game!", justify="center", width=110)
print(Fore.BLUE + welcome_message)
time.sleep(1.5)
print("Here are the rules:\nNumbers will appear on the screen\nIf the number is divisible by 3 type in 'fizz'\nIf the number is divisible by 5 type in 'buzz'\nIf it is divisble by both type in 'fizzbuzz'\nIf its neither type in the number!\nEnjoy!'")

response = input("are you ready to play? (y): ")

if response == "y":
    pass


number_of_players = int(input("Enter the amount of players: "))

for i in range(number_of_players):
    names = input(f"Enter name of player: ")
    players.append(names)

game_running = True
winning_player = "nothing"

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
            lives = 3
            print(f"The number is {count}, you have 5 seconds each question")
            player_ans = input(f"Type in your answer {players[index]}: ")
            check_answer()
            #end_time = time.time()
            #elapsedTime = end_time - start_time
            if player_ans.isdigit() and type(correct_answer) is int:
                ans = int(player_ans)
                if ans == correct_answer:
                    print("correct")
                    count += 1
                    break
                elif ans != correct_answer:
                    if lives == 3:
                        lives -= 1
                        print(f"incorrect you now have {lives} live/s")
                        count += 1
                        break
                    elif lives == 2:
                        lives -= 2
                        print(f"incorrect you now have {lives} live/s")
                        count += 1
                        break
                    elif lives == 1:
                        lives -= 1
                        print(f"incorrect you now have {lives} live/s")
                        count += 1
                        break
                    #print(f"incorrect you now have {lives} live/s")
                    #count += 1
                    #break
                    #index += 1
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
                elif ans != correct_answer:
                    if lives == 3:
                        lives -= 1
                        print(f"incorrect you now have {lives} live/s")
                        count += 1
                        break
                    elif lives == 2:
                        lives -= 2
                        print(f"incorrect you now have {lives} live/s")
                        count += 1
                        break
                    elif lives == 1:
                        lives -= 1
                        print(f"incorrect you now have {lives} live/s")
                        count += 1
                        break
                    #lives -= 1
                    #print(f"incorrect you now have {lives} live/s")
                    #count += 1
                    #break
                    #index += 1
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