import gvt

def print_players(player, opponent):
    print(repr(opponent))
    print()
    print(repr(player))

def take_turn(player, opponent):
    player.start_turn()
    print_players(player, opponent)

    while True:
        command = input(str(player) + " >> ")  # "P 2"
        tokens = command.split()  # ["P", "2"]
        if tokens[0].upper() == "Q":
            break
        elif tokens[0].upper() == "P":
            number = int(tokens[1])
            if player.play_card(number):
                print_players(player, opponent)
            else:
                print("Invalid card.")
        else:
            print("Invalid command.")
       
    # Opponent takes damage 

def main():
    p1_name = input("Enter player 1 name: ")
    player1 = gvt.Player(p1_name, gvt.make_deck(gvt.GOATS))

    p2_name = input("Enter player 2 name: ")
    player2 = gvt.Player(p2_name, gvt.make_deck(gvt.TROLLS))

    player = player1
    opponent = player2

    # Repeat the following until one of the players is defeated.
    take_turn(player, opponent)
    player, opponent = opponent, player

    # Declare the winner and loser.

if __name__ == "__main__":
    main()
