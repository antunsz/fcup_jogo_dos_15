import queue
import random 

class BL:
    
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.pred = {}

    def solve(self):
        start = self.puzzle.initial_board.convert_to_tuple(self.puzzle.initial_board.board)
        pred = {}
        visited = []
        frontier = queue.Queue()
        frontier.put(start)
        
        while frontier.qsize() > 0:
            tmp = frontier.get()
            
            if tmp == self.puzzle.initial_board.goal:
                path = []
                while tmp != start:
                    path.append(pred[tmp][1])
                    tmp = pred[tmp][0]
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
        for k, v in self.pred.items():
            print(k)