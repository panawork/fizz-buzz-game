import pyfiglet
import time 
from colorama import Fore
import sys

# main class
class FizzBuzz:
    def __init__(self):
        self.players = []
        self.count = 1
        self.index = 0
        self.winning_player = ""
        self.correct_answer = 0
        self.playerRegistration = False
        self.x = 0
        self.timer = 5
        self.cheatmodeEnabled = False
        
    # function that contains the introduction and rules of the game
    def introduction(self):
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

    # function that specifies how many players and adds it to the list of players 
    def adding_players(self):
        number_of_players = int(input("Enter the amount of players: "))
        for i in range(number_of_players):
            self.players.append([])
            names = input(f"Enter name of player: ")
            self.players[self.x] += [names]
            self.players[self.x] += [0]
            self.players[self.x] += [3]
            self.x += 1
        self.playerRegistration = True

    # function that checks the answer and puts it into a variable called correct_answer 
    def check_answer(self):
        if self.count % 3 == 0 and self.count % 5 == 0:
            self.correct_answer = "fizzbuzz"
        elif self.count % 3 == 0:
            self.correct_answer = "fizz"
        elif self.count % 5 == 0:
            self.correct_answer = "buzz"
        else:
            self.correct_answer = self.count 

    # main function where the game takes place
    def playGame(self):
        game_running = True
        while self.playerRegistration:
            while game_running:
                for self.index in range(len(self.players)): # loop that goes through each item or index in the players list
                    while self.index < len(self.players): # to make sure that the index loops based on how many players
                        self.check_answer()
                        if self.cheatmodeEnabled: # if the user uses the command --cheatmode then it will show answers
                            print(f"\033[32mYou have entered cheatmode dont tell anyone...\033")
                            print(f"\033[32mthe answer is {self.correct_answer}\033")
                        else:
                            print(f"the number is {self.count}")
                        self.start = time.time()
                        print(f"The number is {self.count}")
                        player_ans = input(f"Type in your answer {self.players[self.index][0]}, you have 5 seconds: ")
                        #self.check_answer()
                        if time.time() - self.start > self.timer:
                            print(f"\033[31mYou took too long {self.players[self.index][0]} you are now eliminated!\033") # eliminates player if they took too long
                            self.players.pop(self.index)
                            if len(self.players) <= 1: # if thers only one player left then end the game 
                                self.winning_player = self.players[0][0]
                                game_running = False
                                break
                            else:
                                self.count += 1
                                break
                        else:
                            if player_ans.isdigit() and type(self.correct_answer) is int: # checks to see if the input is an integer
                                ans = int(player_ans)
                                if ans == self.correct_answer:
                                    print("\U00002705")
                                    self.players[self.index][1] += 1
                                    self.count += 1
                                    #print(self.players)
                                    print(f"Your current score is {self.players[self.index][1]}")
                                    break
                                elif ans != self.correct_answer:
                                    print("\U0000274C")
                                    self.players[self.index][2] -= 1 # if its a wrong answer then player's lives will decrease
                                    if self.players[self.index][2] <= 0:
                                        self.players.pop(self.index)
                                        if len(self.players) <= 1:
                                            self.winning_player = self.players[0][0]
                                            game_running = False
                                            break
                                        else:
                                            self.count += 1
                                            break
                                    else:
                                        print(f"You have {self.players[self.index][2]} lives left")
                                        self.count += 1
                                        break
                            elif isinstance(player_ans, str) and type(self.correct_answer) is str: # checks to see if the players input was a string
                                ans = str(player_ans)
                                if ans == self.correct_answer:
                                    print("\U00002705")
                                    self.players[self.index][1] += 1
                                    #print(self.players)
                                    self.count += 1
                                    print(f"Your current score is {self.players[self.index][1]}")
                                    break
                                elif ans != self.correct_answer:
                                    print("\U0000274C")
                                    self.players[self.index][2] -= 1
                                    if self.players[self.index][2] <= 0:
                                        self.players.pop(self.index)
                                        if len(self.players) <= 1:
                                            self.winning_player = self.players[0][0]
                                            game_running = False
                                            break
                                        else:
                                            self.count += 1
                                            break
                                    else:
                                        self.count += 1
                                        print(f"You have {self.players[self.index][2]} lives left!")
                                        break

                            else:
                                print("incorrect, you are eliminated")
                                self.players.pop(self.index)
                                self.winning_player = self.players[0][0]
                                game_running = False
                                break
                self.index += 1
            print("\U0001F4A3")           
            print(f"\033[31mThe winner is {self.winning_player}\033")
            self.playerRegistration = False


# checks to see if the user or player has inputted a command when running the python file
if len(sys.argv) <= 1:
    cheatmodeEnabled = False
else:
    cheatmodeEnabled = True

# starts automatically when file is played 
if __name__ == "__main__":
    start_game = FizzBuzz()
    #start_game.introduction()
    start_game.adding_players()
    start_game.cheatmodeEnabled=cheatmodeEnabled
    start_game.playGame()
