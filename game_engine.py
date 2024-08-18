from typing import NamedTuple, Optional, List
import random

class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None

# ----------------------------
def get_answer(question: str, options: str) -> str:
    ''' Get an answer '''

    while True:
        answer = input(question)
        if not (answer in options and answer.isalnum()):
            print(f'Invalid choice "{answer}". Possible options are {list(options)}.')
        else:
            break
    return answer

# ----------------------------
def format_board(board: List[str]) -> str:
    ''' Get formatted board '''

    board = [count if number == '.' else number for count, number in enumerate(board, 1)]

    return '\n'.join([ 
        f'{board[0]}|{board[1]}|{board[2]}',
        '-+-+-',
        f'{board[3]}|{board[4]}|{board[5]}',
        '-+-+-',
        f'{board[6]}|{board[7]}|{board[8]}'])

# ----------------------------
def get_move(state: State, human: str) -> State:
    ''' Get the player's move '''

    player = state.player

    if player == human:
        move = input(f'What is your move, {player}? Or press "q" to quit the game: ')

        if move == 'q':
            return state._replace(quit=True)
    
        if not (move.isdigit() and int(move) in range(1, 10)):
            return state._replace(error=f'Invalid move "{move}"! Use 1-9.')
    
        move_number = int(move)
        if state.board[move_number - 1] in 'XO':
            return state._replace(error=f'Cell "{move}" is already taken!')
    else:
        pc_options = [str(count) for count, position in enumerate(state.board, 1) if position == '.']
        pc_choice = random.choice(pc_options)  
        move_number = int(pc_choice)  

    board = state.board
    board[move_number - 1] = player
    return state._replace(board=board,
                          player='O' if player == 'X' else 'X',
                          winner=find_winner(board),
                          draw='.' not in board,
                          error=None)  

# --------------------------------------------------
def reset_state(state: State) -> State:
    return state._replace(board=list('.' * 9))

# --------------------------------------------------
def find_winner(board: List[str]) -> str:
    """ Determine if there is a winner """

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in 'XO':
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player
