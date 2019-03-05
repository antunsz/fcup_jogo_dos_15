class Checker:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def _check_grid_position(self):
        linha = 1
        count = 1
        for i, value in enumerate(self.puzzle.initial_config):
            if count == self.puzzle.matrix_width:
                linha += 1
                count = 0
            if 0 in self.puzzle.initial_config[i:i+self.puzzle.matrix_width]:
                break
            count += 1
        if linha % 2 == 0:
            return True
        else:
            return False

    def _solubility_rules(self):
        rule = "par"
        #first rule
        if len(self.puzzle.initial_config) %2 == 0:
            #second rule
            if self._check_grid_position():
                #solução impar
                rule = "par"
            else:
                #third rule
                rule = "impar"
                    
        if rule == "par":
            return False if self.puzzle.points % 2 == 0 else True
        if rule =="impar":
            return True if self.puzzle.points % 2 == 0 else False        


    def there_is_no_solution(self):
        points  = 0
        for i, value in enumerate(self.puzzle.initial_config):
            if self.puzzle.initial_config[i] == 0:
                self.puzzle.points += 0
            else:
                self.puzzle.points += len([x for x in self.puzzle.initial_config[i:] if x < value and x != 0])
                print(f"Position={i} |Pontos = {self.puzzle.points} | inversões = {len([i for i in self.puzzle.initial_config[value:] if i > value])}")

        return self._solubility_rules()

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
                print(str(f"position: {i} - error: {e}"))

        self.final_tree = tree 
    
    def print_tree(self, tree):
        layer = tree
        for _ in range(len(self.final_config)+1):
            for node in layer:
                print(node)
            layer = layer[0].children

class Node:
    "Generic tree node."
    def __init__(self, value='root', children=None, puzzle_position=None):
        self.value = value
        self.puzzle_position = puzzle_position
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return str(self.value)

    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)

class Board:
    def __init__(self, board_array, width=4):
        # 4 by 4 board
        # self.board is the goal board when first initialized
        self.board = self._generate_matrix(width, board_array)
        # self.goal is later used as a comparison to solve the mixed board
        self.goal = [] 
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        # self.empty is the position of empty block TODO
        self.empty = self._locate_blank()

    def _generate_matrix(self, matrix_width, array):
        matrix = []
        count = 0
        aux = []
        for p, i in enumerate(array):
            if count < matrix_width:
                aux.append(i)
                count += 1
                if p+1 == len(array):
                    matrix.append(aux[:])
            else:
                matrix.append(aux[:])
                aux = []
                aux.append(i)
                count = 1
        return matrix

    def _locate_blank(self, matrix=None):
        if not matrix:
            matrix=self.board
            
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    return [i,j]

    def move_up(self): # move empty block up
        try:
            if self.empty[0] != 0:
                tmp = self.board[self.empty[0]-1][self.empty[1]]
                self.board[self.empty[0]-1][self.empty[1]] = 0
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0]-1, self.empty[1]]
        except IndexError:
            pass

    def move_down(self): # move empty block down
        try:
            tmp = self.board[self.empty[0]+1][self.empty[1]]
            self.board[self.empty[0]+1][self.empty[1]] = 0
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0]+1, self.empty[1]]
        except IndexError:
            pass

    def move_right(self): # move empty block right
        try:
            tmp = self.board[self.empty[0]][self.empty[1]+1]
            self.board[self.empty[0]][self.empty[1]+1] = 0
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0], self.empty[1]+1]
        except IndexError:
            pass

    def move_left(self): # move empty block left
        try:
            if self.empty[1] != 0:
                tmp = self.board[self.empty[0]][self.empty[1]-1]
                self.board[self.empty[0]][self.empty[1]-1] = 0
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0], self.empty[1]-1]
        except IndexError:
            pass


    def __repr__(self):
        string = ''
        for row in self.board:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string

class BL:
    pass