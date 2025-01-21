import random
#user sees indented message
VALID_CHOICES = ['r', 'c', 'p', 'l', 's']
player_win_count = 0
computer_win_count = 0


def match_win_or_lose(player_win_count, computer_win_count):

    if player_win_count < 3 and computer_win_count < 3:
        prompt("Play again")


    elif player_win_count >= 3:
        prompt("You Win the match!")


    else:
        prompt("Computer wins the match!")
        player_win_count = 0
        computer_win_count = 0

def prompt(message):
    print(f"==> {message}")



def display_winner(player, computer):
    global computer_win_count, player_win_count
    winning_cases = {
        'r': {'c', 'l'},
        'p': {'r', 's'},
        'c': {'p', 'l'},
        'l': {'p', 's'},
        's': {'r', 'c'},
    }
    prompt(f"You chose {player}, computer chose {computer}")

    if player in winning_cases:
        player_win_count += 1
        prompt(f"You win.  Player has {player_win_count} wins."
               f"Computer has {computer_win_count} wins")


    elif  computer in winning_cases:

        computer_win_count += 1
        prompt(f"Computer wins! Player has {player_win_count} wins.  "
               f"Computer has {computer_win_count} wins")


    else:
        prompt(f"It's a tie! Player has {player_win_count}"
               f" wins.  Computer has {computer_win_count}"
                " wins")

answer = "y"

while answer != "n":

    while computer_win_count < 3 and player_win_count < 3:
        prompt(f"Choose one: {", ".join(VALID_CHOICES)}, r "
               "for rock, p for paper, c for scissors, s for spock,"
                " or l for lizard.")
        choice = input()
        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        display_winner(choice, computer_choice)
        match_win_or_lose(player_win_count, computer_win_count)

    prompt("Do you want to play again (y/n)")
    answer = input().lower()
    while answer not in ("y", "n"):
        prompt("That's not a valid choice")
        answer = input().lower()

    