import queue 
import timeit
import sys

class BL:
    
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.pred = None
        self.frontier = None
        self.solution = None
        self.time = None

    def search_solution(self):
        self.time = timeit.timeit(self._search_solution, number=1)

    def _search_solution(self):
        start = self.puzzle.initial_board.convert_to_tuple(self.puzzle.initial_board.board)
        pred = {}
        visited = []
        frontier = queue.Queue()
        frontier.put(start)
        
        #enquanto ainda existirem nós para serem visitados
        while frontier.qsize() > 0:
            tmp = frontier.get()
            #se a variável tmp for igual à configuração final
            if tmp == self.puzzle.final_board.goal:
                path = []
                #enquanto a variável tmp for diferente da minha configuração final (voltando no grafo)
                while tmp != start:
                    #adiciona no path o passo neste instante de tempo
                    path.append(pred[tmp][1])
                    #adiciona no tmp a próxima configuração 
                    tmp = pred[tmp][0]
                #salva na classe a solução ótima  invertendo a sua posição (o último objeto é o primeiro da solução)  
                self.solution = path[::-1]
                return path[::-1]

            if tmp not in visited:
                visited.append(tmp)
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_up()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'up']

                
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_down()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'down']

                        
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_right()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'right']

                
                tmpboard = self.puzzle.match(tmp)
                tmpboard.move_left()
                if self.puzzle.initial_board.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.puzzle.initial_board.convert_to_tuple(tmpboard.board))
                    if not self.puzzle.initial_board.convert_to_tuple(tmpboard.board) in pred:
                        pred[self.puzzle.initial_board.convert_to_tuple(tmpboard.board)]=[tmp, 'left']
            
        
        self.pred = pred    

        raise Exception('There is no solution.')

    def show_solution(self):
        print(self.solution)

    def show_time(self):
        #TODO: transformar em segundos
        print(self.time)

    def show_size(self):
        print(sys.getsizeof(self.pred))

    def solve(self):
        if not self.solution:
            print("A busca ainda não foi executada. hint: utilize o método .search_solution()")
        else:
            tmp_board = self.puzzle.initial_board
            for step in self.solution:
                print("Movimento do espaço em branco:", step)
                self._control_board(tmp_board, step)
                print(tmp_board)

    def _control_board(self, board, step):
        if step == 'up':
            board.move_up()
        elif step == 'down':
            board.move_down()
        elif step == 'left':
            board.move_left()
        elif step == 'right':
            board.move_right()
        else:
            print("Passo não reconhecido.")    

