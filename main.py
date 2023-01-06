# Tic Tac Toe Game!

answer_list = {
    "a1": " ",
    "a2": " ",
    "a3": " ",
    "b1": " ",
    "b2": " ",
    "b3": " ",
    "c1": " ",
    "c2": " ",
    "c3": " ",
}


def play_game():
    """Prompt user to play Tic Tac Toe"""
    play_again = input("\nWould you like to play Tic Tac Toe? (y/n): ")
    if play_again == 'y':
        for x in answer_list:
            answer_list[x] = " "
        tic_tac_toe()
    else:
        pass


def game_board():
    """Create the Game Board"""
    the_board = (
        "\n"
        "\n   | 1 | 2 | 3 "
        "\n---|-----------"
        f'\n A | {answer_list["a1"]} | {answer_list["a2"]} | {answer_list["a3"]}'
        "\n---|-----------"
        f'\n B | {answer_list["b1"]} | {answer_list["b2"]} | {answer_list["b3"]}'
        "\n---|-----------"
        f'\n C | {answer_list["c1"]} | {answer_list["c2"]} | {answer_list["c3"]}'
        "\n\n======================================================================"
        "\n\n"
    )

    return the_board


def tic_tac_toe():
    """Logic to determine if a player-entered coordinate exists and is available."""
    print("\n=== Welcome to Tic Tac Toe! ===")

    game_on = True
    turns = 0
    print(game_board())

    while game_on:

        # Determine which player's turn it is
        if turns % 2 == 0:
            player_symbol = "X"
        else:
            player_symbol = "O"

        # Prompt player for coordinate
        player_answer = input(f"Turn {turns + 1}: Player {player_symbol}, enter a coordinate (example: B2) to place your '{player_symbol}': ").lower()

        # Check if coordinate exists and is available
        if player_answer not in answer_list:
            print("\n[[[ Please enter a valid coordinate (A1 to C3). ]]]\n")
        elif answer_list[player_answer] == " ":
            answer_list[player_answer] = player_symbol
            print(game_board())
            turns += 1
            game_on = check_winner(turns)
        else:
            print(f"\n[[[ {player_answer.upper()} is taken. Please choose another coordinate. ]]]\n")
        

    play_game()


def check_winner(turns):
    """Checks the latest coordinate entered against previous entries to determine if there is a winner"""
    winners = [
        [answer_list["a1"], answer_list["a2"], answer_list["a3"]],
        [answer_list["b1"], answer_list["b2"], answer_list["b3"]],
        [answer_list["c1"], answer_list["c2"], answer_list["c3"]],
        [answer_list["a1"], answer_list["b1"], answer_list["c1"]],
        [answer_list["a2"], answer_list["b2"], answer_list["c2"]],
        [answer_list["a3"], answer_list["b3"], answer_list["c3"]],
        [answer_list["a1"], answer_list["b2"], answer_list["c3"]],
        [answer_list["a3"], answer_list["b2"], answer_list["c1"]],
    ]

    for trio in winners:
        if all(i == 'X' for i in trio):
            print('\n\n!!!!! Player X is the winner !!!!!\n\n')
            return False
        if all(i == 'O' for i in trio):
            print('\n\n!!!!! Player O is the winner !!!!!\n\n')
            return False
        elif turns > 8:
            print("!!!!! It's a DRAW !!!!!")
            return False
    print("\nNo winner yet. Keep playing!\n")
    return True


play_game()
