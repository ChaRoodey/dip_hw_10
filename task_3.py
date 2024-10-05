class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]
        self.win_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
                        {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        self.current_x_cells = []
        self.current_o_cells = []

    def change_cell(self, cell_id, char):
        if self.cells[cell_id].available:
            self.cells[cell_id].char = char
            self.cells[cell_id].available = False
            print('Ход записан!')
        else:
            print('Ячейка занята!')

    # 123 456 789 147 258 369 159 357
    def is_game_ended(self):
        self.current_x_cells = {i + 1 for i in range(9) if self.cells[i].char == 'X'}
        self.current_o_cells = {i + 1 for i in range(9) if self.cells[i].char == 'O'}
        for configuration in self.win_set:
            if configuration.issubset(self.current_x_cells):
                return 'x'
            elif configuration.issubset(self.current_o_cells):
                return 'o'
        if len(self.current_o_cells) + len(self.current_x_cells) == 9:
            return ' '


class Cell:
    def __init__(self, cell_id: int):
        self.cell_id = cell_id
        self.available = True
        self.char = ' '


class Player:
    def __init__(self, name, char: str):
        self.name = name
        self.char = char


class Game:
    def __init__(self, p1, p2: str):
        self.board = Board()
        self.cell_id = 0
        self.char = ''
        self.game_status = 'Started'
        self.player_x = Player(p1, 'X')
        self.player_o = Player(p2, 'O')
        self.start_game()

    def start_game(self):
        print('Игра крестики нолики.')
        print(f'{self.player_x.name} играет за "X", {self.player_o.name} играет за "O"')
        for cell in self.board.cells:
            if not cell.available:
                cell.available = True
                cell.char = ' '
        self.print_board()
        self.progress_game(self.player_x, self.player_o)

    def progress_game(self, curr_player, other_player):
        print(f'{curr_player.name} сделайте ход. Введите')

        self.cell_id = int(input('Номер ячейки: ')) - 1

        if self.cell_id > 10 or self.cell_id < 0:
            print('Некорректный номер ячейки. Введите номер от 1 до 6')
            self.progress_game(curr_player, other_player)

        else:
            self.make_move(self.cell_id, curr_player.char)

        if self.board.is_game_ended() == 'x':
            self.game_ending(' ' + self.player_x.name)
        elif self.board.is_game_ended() == 'o':
            self.game_ending(' ' + self.player_o.name)
        elif self.board.is_game_ended() == ' ':
            self.game_ending('а дружба')
        else:
            self.progress_game(other_player, curr_player)

    def game_ending(self, winner):
        if input(f'Игра окончена. Победил{winner} 1 - новая игра, 2 - выйти: ') == '1':
            self.start_game()

    def make_move(self, cell_id: int, char: str):
        self.board.change_cell(cell_id, char)
        self.print_board()

    def print_board(self):
        for i in range(0, len(self.board.cells), 3):
            print(f'|{self.board.cells[i].char}|{self.board.cells[i + 1].char}|{self.board.cells[i + 2].char}|')


if __name__ == '__main__':
    game = Game('Олег', 'Какой-то пидор')