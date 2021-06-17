# Tic-Tac-Toe

from enum import IntEnum


def main():
    Game().start()


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
        bi = 0
        print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
        print("   -----")
        bi += self.size
        print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
        print("   -----")
        bi += self.size
        print("   %s|%s|%s" % tuple([board[i] for i in range(bi, bi + self.size)]))
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

    def __init__(self):
        self.__winner = None
        self.__xPlayer = GamePlayer('Player 1', 'X')
        self.__oPlayer = GamePlayer('Player 2', 'O')
        self.__firstPlayer = self.__xPlayer
        self.__board = GameBoard(3, self.__xPlayer, self.__oPlayer)

    def start(self):
        self.__print_intro()
        self.__state = GameState.NOT_DONE

        self.__move = 0

        while self.game_not_over():
            self.take_turn()
            self.find_winner()

            if self.reached_max_moves() and not self.has_winner():
                self.__state = GameState.CAT

            self.__board.print_board()
            self.__print_winner()

    def __print_winner(self) -> None:
        if self.__winner is not None:
            print("%s Wins!!!" % self.__winner.name)
        elif self.__state == GameState.CAT:
            print("Cat's game")

    def find_winner(self) -> None:
        self.__winner = self.__board.get_winner(self.get_current_player())
        if self.has_winner():
            self.__state = GameState.GAME_WON

    def has_winner(self) -> bool:
        return self.__winner is not None

    def __print_intro(self) -> None:
        print("Tic-Tac-Toe Game (%s x %s)" % (self.__board.size, self.__board.size))
        print("q to quit\n")
        self.__board.print_help()

    def game_not_over(self) -> bool:
        return self.__state == GameState.NOT_DONE

    def take_turn(self) -> None:
        new_mark = self.get_user_input()
        self.__board.update(new_mark, self.get_current_player())
        self.__move += 1

    def get_user_input(self) -> int:
        bad_input = True
        while bad_input:
            square = self.__get_raw_input()

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

    def __get_raw_input(self) -> str:
        return input("%s make your move. " % self.get_current_player().name)

    def get_current_player(self) -> GamePlayer:
        return self.__xPlayer if self.__move % 2 == 0 else self.__oPlayer

    def reached_max_moves(self) -> bool:
        return self.__move == self.__board.allowed_moves()

    def game_won(self) -> bool:
        return self.__winner is not None


if __name__ == '__main__':
    main()
