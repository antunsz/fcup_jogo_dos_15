from utils.Checker import Checker
from utils.Puzzle import Puzzle
from utils.BL import BL

#estado de partida onde existe uma solução
initial_config = [1,2,3,4,5,6,8,12,13,9,0,7,14,11,10,15]

#estado de partida onde não existe solução
initial_config2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,0]

#estado final
final_config =   [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

#objeto puzzle
puzzle = Puzzle(4, initial_config, final_config)

#objecto que checará se o puzzle possui solução ou não
checker = Checker(puzzle)

#método que inicial o jogo
def init_game():
    #verifica se existe solução para o problema TODO:validar se as duas configurações (inicial e final) possuem solução
    if checker.there_is_no_solution():
        print("Sem solução")
    else:
        #série de teste, pode-se remover
        #print(checker.puzzle.points)
        #print(puzzle.number_out_of_place())
        #puzzle.print_tree(puzzle.final_tree)
        #print(puzzle.initial_board)
        #print(puzzle.initial_board.board)
        #print("mover para cima")
        #puzzle.initial_board.move_up()
        #print(puzzle.initial_board)
        #print(puzzle.final_board)

        print("-"*10+"Busca em Largura"+"-"*10)
        #objeto de busca em largura passando o puzzle
        bl = BL(puzzle)
        print("Antes")
        bl.show_size()
        #resolve a busca
        bl.search_solution()
        print("Profundidade:", len(bl.solution))
        print("Passos para resolução:", bl.solution)
        #mostra o conjunto de estados solução
        #bl.show_solution()
        #mostra as fronteiras
        #bl.show_frontier()
    
        #puzzle.initial_board.move_down()
        print("-"*15)
        bl.solve()

        print(bl.time)

        print("Tamanho depois")
        bl.show_size()
if __name__ == "__main__":
    assert len(initial_config) == len(final_config), "Os tabuleiros devem possuir o mesmo tamanho."
    
    init_game()
    
