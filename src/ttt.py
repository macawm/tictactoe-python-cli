# Tic-Tac-Toe

from enum import IntEnum


def main():
    Game(GamePlayer('Player 1', 'X'), GamePlayer('Player 2', 'O')).start()


class GameState(IntEnum):
    NOT_DONE = -1
    CAT = 0
    GAME_WON = 1


class GamePlayer:
    def __init__(self, name: str, marker: str):
        self.name = name
        self.marker = marker


class GameBoard:
    def __init__(self, size: int, p1: GamePlayer, p2: GamePlayer):
        self.size = size  # TODO handle different size boards
        self.__helpInfo = [i for i in range(1, self.size**2 + 1)]
        self.__data = [' ' for _ in range(self.size**2)]

        self.__player1 = p1
        self.__player2 = p2

    def print_help(self) -> None:
        self.__print_board(self.__helpInfo)

    def print_board(self) -> None:
        self.__print_board(self.__data)

    def __print_board(self, board: list) -> None:
        inset = '   '
        for row in range(self.size):
            r_c = row * self.size
            row_str = ''.join(('%%s%s' % ('\u2502' if x != self.size-1 else '')) for x in range(self.size))
            print(inset + row_str % tuple([board[i] for i in range(r_c, r_c + self.size)]))
            if row != self.size - 1:
                print(inset + "\u2500\u253c\u2500\u253c\u2500")
        print()

    def square_in_range(self, s_int: int) -> bool:
        return s_int in range(1, self.size**2 + 1)

    def square_is_open(self, s_int: int) -> bool:
        if self.square_in_range(s_int):
            return self.mark_at_square(s_int) == ' '
        else:
            return False

    def allowed_moves(self) -> int:
        return self.size**2

    def get_winner(self, player: GamePlayer) -> GamePlayer:
        return player if self.__did_win(player.marker) else None

    def __did_win(self, mark: str) -> bool:
        win = False
        for bi in range(self.size):
            win = win or (self.__data[bi*self.size] == mark and self.__data[bi*self.size+1] == mark and self.__data[bi*self.size+2] == mark)
            win = win or (self.__data[bi] == mark and self.__data[bi+self.size] == mark and self.__data[bi+self.size*2] == mark)

        bi = 0
        # diag l
        win = win or (self.__data[bi] == mark and self.__data[bi+4] == mark and self.__data[bi+8] == mark)

        bi = 2
        # diag r
        win = win or (self.__data[bi] == mark and self.__data[bi+2] == mark and self.__data[bi+4] == mark)

        return win

    def update(self, square: int, player: GamePlayer) -> None:
        """ This is the first, of only two, places where we alter the user input to correspond with our data store. """
        if self.square_in_range(square):
            self.__data[square - 1] = player.marker

    def mark_at_square(self, square: int) -> str:
        """ This is the second, of only two, places where we alter the user input to correspond with our data store. """
        if self.square_in_range(square):
            return self.__data[square-1]


class Game:
    __state = None
    __move = None

    def __init__(self, p1: GamePlayer, p2: GamePlayer):
        self.__winner = None
        self.__move = 0
        self.__state = GameState.NOT_DONE

        self.__xPlayer = p1
        self.__oPlayer = p2
        self.__firstPlayer = self.__xPlayer

        self.__board = GameBoard(3, self.__xPlayer, self.__oPlayer)

    def start(self):
        self.__print_intro()

        while self.__game_not_over():
            self.take_turn()

            if self.__reached_max_moves() and not self.__has_winner():
                self.__state = GameState.CAT

            self.__board.print_board()
            self.__print_winner()

    def __print_winner(self) -> None:
        if self.__winner is not None:
            print("%s Wins!!!" % self.__winner.name)
        elif self.__state == GameState.CAT:
            print("Cat's game")

    def __find_winner(self) -> None:
        self.__winner = self.__board.get_winner(self.get_current_player())
        if self.__has_winner():
            self.__state = GameState.GAME_WON

    def __has_winner(self) -> bool:
        return self.__winner is not None

    def __print_intro(self) -> None:
        print("Tic-Tac-Toe Game (%s x %s)" % (self.__board.size, self.__board.size))
        print("q to quit\n")
        self.__board.print_help()

    def __game_not_over(self) -> bool:
        return self.__state == GameState.NOT_DONE

    def take_turn(self) -> None:
        new_mark = self.get_user_input()
        self.__board.update(new_mark, self.get_current_player())

        self.__find_winner()
        self.__move += 1

    def get_user_input(self) -> int:
        bad_input = True
        while bad_input:
            square = input("%s make your move. " % self.get_current_player().name)

            if square.isdigit():
                s_int = int(square)
                if not self.__board.square_is_open(s_int):
                    print("Bad selection. Try again.")
                    bad_input = True
                else:
                    bad_input = False
            elif square == 'q':
                quit()
            else:
                print("Bad selection. Try again.")
                bad_input = True

        return s_int

    def get_current_player(self) -> GamePlayer:
        return self.__xPlayer if self.__move % 2 == 0 else self.__oPlayer

    def __reached_max_moves(self) -> bool:
        return self.__move == self.__board.allowed_moves()

    def game_won(self) -> bool:
        return self.__winner is not None


if __name__ == '__main__':
    main()
