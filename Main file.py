import random

#Function to show game board
def show_board(board) :
    for i in range(9) :
        if i%3 == 0 and i>0 :
            print('\n')
        print(f" {board[i]} ", end="|") if (i + 1) % 3 != 0 else print(f" {board[i]} ")

#Functiom to take player's choice
def player_choice(index,board,player_move) :
    ind = int(input("Enter the index (0-8) at which you want to play :"))
    while(ind > 9 and ind>0 and ind in index) :
        print("Invalid or choose index already played. Choose again : ")

        ind = int(input("Enter the index (0-8) at which you want to play :"))

    index.append(ind)
    board[ind] = player_move

#Function to make computer's choice
def computer_choice(board,index,comp_move) :
    ind = random.randint(0,8)
    while(ind in index) :
        ind = random.randint(0,8)
    index.append(ind)
    board[ind] = comp_move

#Function to check win
def win_check(board) :
    win_combos = [[0,1,2], [3,4,5] , [6,7,8],
                  [0,3,6], [1,4,7], [2,5,8],
                  [0,4,8],[2,4,6]]
    for combo in win_combos :
        if(board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ") :
            return 1
    return 0

#Game board
board = [" " for i in range(9)]
index = []

player_move = input("Choose your play choice : (X/O) ").upper()

while player_move not in ["X","O"]:
    player_move = input("Please choose from (X/O) : ").upper()

comp_move = "O" if player_move == "X" else "X"

count = 0

print("Initial Board : ")
show_board(board)

while(count < 9) : 
    print("\nYour Turn : ")
    player_choice(index,board,player_move)

    show_board(board)

    win = win_check(board)
    if win == 1 :
        print(f"Winner is {player_move}")
        break

    print("\nComputer's Turn:")
    computer_choice(board, index, comp_move)
    show_board(board)

    win = win_check(board)
    if win == 1 :
        print(f"Winner is {comp_move}")
        break

    count += 2    

else :
    print("Game Draw !")   
