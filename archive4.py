import pyfiglet
import time 
from colorama import Fore

# Archive where I implemented the double list in order to add a score and lives.

class FizzBuzz:

    def __init__(self):
        self.players = []
        self.count = 1
        self.index = 0
        self.winning_player = ""
        self.correct_answer = 0
        self.playerRegistration = False
        self.x = 0

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
            self.players[self.x] += [names] # sets the names for every players since it is a double list
            self.players[self.x] += [0] # sets the scores to 0 for every player
            self.players[self.x] += [3] # sets the lives to 3 for each player
            self.x += 1
        #print(self.players)
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
                for self.index in range(len(self.players)):
                    while self.index < len(self.players):
                        print(f"The number is {self.count} and everyone has 3 lives!")
                        player_ans = input(f"Type in your answer {self.players[self.index][0]}: ")
                        self.check_answer()
                        if player_ans.isdigit() and type(self.correct_answer) is int:
                            ans = int(player_ans)
                            if ans == self.correct_answer:
                                print("correct")
                                self.players[self.index][1] += 1 # adds 1 point to the score 
                                self.count += 1
                                #print(self.players)
                                print(f"Your current score is {self.players[self.index][1]}")
                                break
                            elif ans != self.correct_answer:
                                print("incorrect")
                                self.players[self.index][2] -= 1 # takes away 1 life
                                if self.players[self.index][2] <= 0:
                                    self.players.pop(self.index)
                                    if len(self.players) <= 1:
                                        self.winning_player = self.players[0][0]
                                        #print(self.players)
                                        game_running = False
                                        break
                                    else:
                                        #print(self.players)
                                        self.count += 1
                                        break
                                else:
                                    #print(self.players)
                                    print(f"You have {self.players[self.index][2]} lives left") # displays how many lives left
                                    self.count += 1
                                    break
                        elif isinstance(player_ans, str) and type(self.correct_answer) is str:
                            ans = str(player_ans)
                            if ans == self.correct_answer:
                                print("correct")
                                self.players[self.index][1] += 1
                                self.count += 1
                                print(f"Your current score is {self.players[self.index][1]}")
                                break
                            elif ans != self.correct_answer:
                                print("incorrect")
                                self.players[self.index][2] -= 1
                                if self.players[self.index][2] <= 0:
                                    self.players.pop(self.index)
                                    if len(self.players) <= 1:
                                        self.winning_player = self.players[0][0]
                                        #print(self.players)
                                        game_running = False
                                        break
                                    else:
                                        #print(self.players)
                                        self.count += 1
                                        break
                                else:
                                    #print(self.players)
                                    self.count += 1
                                    print(f"You have {self.players[self.index][2]} lives left!")
                                    break
                        else:
                            print("incorrect, you are eliminated")
                            self.players.pop(self.index)
                            self.winning_player = self.players[0]
                            print(self.players)
                            game_running = False
                            break
                self.index += 1               
            print(f"The winner is {self.winning_player}")
            self.playerRegistration = False


if __name__ == "__main__":
    start_game = FizzBuzz()
    start_game.introduction()
    start_game.adding_players()
    start_game.playGame()