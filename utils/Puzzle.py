from utils.Board import Board
from utils.Node import Node

class Puzzle:

    def __init__(self, matrix_width, initial_config, final_config):
        self.initial_config = initial_config
        self.final_config = final_config
        self.matrix_width = matrix_width
        self.final_tree = None
        self.initial_board = Board(initial_config, matrix_width)
        self.final_board = Board(final_config, matrix_width)
        self.points = 0
        #methods
        self._generate_final_tree()

    def number_out_of_place(self):
        return len([i for i, value in enumerate(self.initial_config) if value != self.final_config[i]])

    def manhattan_distance(self):
        return 
    
    def _generate_final_tree(self):
        tree = [Node()]
        layer = tree
        for i, value in enumerate(self.final_config):
            try:
                layer[0].add_child(Node(value=value, puzzle_position=i+1))
                layer = layer[0].children
            except Exception as e:
                print(str("position: {} - error: {}".format(i, e)))

        self.final_tree = tree 
    
    def print_tree(self, tree):
        layer = tree
        for _ in range(len(self.final_config)+1):
            for node in layer:
                print(node)
            layer = layer[0].children

    def match(self, copy):
        a = Board()
        a.board = copy
        for row in range(0, 4):
            for col in range(0, 4):
                if a.board[row][col] == 0:
                    a.empty = [row, col]
        result = []
        for i in a.board:
            result.append(list(i))
        a.board = result
        return a