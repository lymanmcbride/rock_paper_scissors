import random

total_games = 0
game_win = 0
rounds_played = 0
user_wins = 0
computer_wins = 0
log = []
user = ""
#main program functions
def main():
    print("Hello! Lets play rock, paper, scissors!")
    get_games()
    analyze()

def analyze():
    global rounds_played
    global user_wins
    global computer_wins
    computer_choice, user_choice = get_choices()
    if user_choice == computer_choice:
        print("You both chose {}!".format(user_choice))
        #!!may want to add the round to the list once we set up the datastructure
        analyze()
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print ("You won! The computer chose {} and you chose {}.".format(computer_choice, user_choice))
        rounds_played += 1
        user_wins += 1
        log.append([rounds_played, user_choice, computer_choice, user])
        last()
    else:
        print ("You lost! The computer chose {} and you chose {}.".format(computer_choice, user_choice))
        rounds_played += 1
        computer_wins += 1
        log.append([rounds_played, user_choice, computer_choice, "computer"])
        last()
def last():
    print(game_win, rounds_played, user_wins, computer_wins)
    if user_wins < game_win:
        if computer_wins < game_win:
            if rounds_played == total_games:
                print("The next round is sudden death! Whoever wins will win the whole game!")
            his = input("Would you like to see the game history? y/n").lower()
            if his == "y":
                history()
            analyze()
        else:
            if user_wins > computer_wins:
                print("You won the whole game! Here are you stats:")
                print("Your wins: {}\nComputer wins:{}\n".format(user_wins, computer_wins))
                history()
                quit = input("When you are done, please type quit").lower()
                print("Thank you for playing our game!, have a nice day!")
            else:
                print("You lost the whole game! Here are the stats:")
                print("Your wins: {}\nComputer wins:{}".format(user_wins, computer_wins))
                history()
                quit = input("When you are done, please type quit").lower()
                print("Thank you for playing our game!, have a nice day!")

#getting functions
def get_choices():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_choice = input("Please choose rock, paper, or scisssors by typing your choice now.\n").lower()
    return computer_choice, user_choice
def get_games():
    global total_games
    global game_win
    user = input("What is your name?\n").title()
    total_games = int(input("How many games would you like to play to?\n"))
    game_win = (total_games//2) + 1
def history():
    for list_element in log:
        print("Game {}\nWinner: {}\nYou chose: {}\nComputer chose: {}\n\n".format(list_element[0], list_element[3], list_element[1], list_element[2]))


main()