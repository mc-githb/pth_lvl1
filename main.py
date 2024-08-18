import game_engine as ge

def main() -> None:
    ''' This is where the magic happens '''

    action = ge.get_answer('\n'.join([
        'What would you like to do?',
        '1 - Start a new game',
        '2 - Quit\n']), '12')

    if action == '2':
        print("\033[H\033[J")
        print('Thank you. Come again!')
    else:
        player = ge.get_answer('Pick a side: X or O? ', 'XO')

        state = ge.State()

        if player == 'O':
            state = state._replace(player='O')
            
        while True:
            print("\033[H\033[J")
            print(ge.format_board(state.board))

            if state.error:
                print(state.error)
            elif state.winner:
                print(f'Player "{state.winner}" has won! Congrats!')
                break

            state = ge.get_move(state, player)

            if state.quit:
                print('You lose!')
                break
            elif state.draw:
                print('It is a draw!')
                break
        
        # board = state.board
        # board = list('.' * 9)
        # state = state._replace(board=board)
        ge.reset_state(state)
        state = ''
        main()

if __name__ == '__main__':
    main()