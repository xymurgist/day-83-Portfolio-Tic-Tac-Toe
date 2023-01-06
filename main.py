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


def play_tic_tac_toe():
    print("\n=== Welcome to Tic Tac Toe! ===")

    game_on = True
    turns = 0

    while game_on:

        print("\n")
        print("   | 1 | 2 | 3 ")
        print("---|-----------")
        print(f' A | {answer_list["a1"]} | {answer_list["a2"]} | {answer_list["a3"]}')
        print("---|-----------")
        print(f' B | {answer_list["b1"]} | {answer_list["b2"]} | {answer_list["b3"]}')
        print("---|-----------")
        print(f' C | {answer_list["c1"]} | {answer_list["c2"]} | {answer_list["c3"]}')
        print("\n======================================================================")
        print("\n\n")


        if turns % 2 == 0:
            player_symbol = "X"
        else:
            player_symbol = "O"


        player_answer = input(f"Turn {turns + 1}: Player {player_symbol}, enter a coordinate (example: B2) to place your '{player_symbol}': ").lower()

        if player_answer not in answer_list:
            print("\n!!!!! Please enter a valid coordinate (example: B2). !!!!!")
        elif answer_list[player_answer] == " ":
            answer_list[player_answer] = player_symbol
            turns += 1
        else:
            print("\n!!!!! That coordinate is taken. Please choose another coordinate. !!!!!")

        game_on = check_winner(turns)

    play_game()


def check_winner(turns):
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

    if turns > 9:
        print("It's a DRAW!")
        return False

    for trio in winners:
        if all(i == 'X' for i in trio):
            print('\n\n!!!!! Player X is the winner !!!!!\n\n')
            return False
        if all(i == 'O' for i in trio):
            print('\n\n!!!!! Player O is the winner !!!!!\n\n')
            return False
    print("No winner yet. Keep playing!")
    return True


def play_game():
    play_again = input("\nWould you like to play Tic Tac Toe? (y/n): ")
    if play_again == 'y':
        for x in answer_list:
            answer_list[x] = " "
        play_tic_tac_toe()
    else:
        pass


play_game()