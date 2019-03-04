from utils import Checker, Puzzle


initial_config = [1,2,3,4,5,6,8,12,13,9,0,7,14,11,10,15]
final_config =   [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

puzzle = Puzzle(4, initial_config, final_config)
checker = Checker(puzzle)

def init_game():
    if checker.there_is_no_solution():
        return False
    else:
        return True
    

if __name__ == "__main__":
    assert len(initial_config) == len(final_config), "Os tabuleiros devem possuir o mesmo tamanho."
    
    init_game()
    print(checker.puzzle.points)
    print(puzzle.number_out_of_place())
    puzzle.print_tree(puzzle.final_tree)
