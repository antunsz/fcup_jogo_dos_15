import math

matrix_width = 4



initial_config = [1,2,3,4,5,6,8,12,13,9,0,7,14,11,10,15]
final_config = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

def _solubility_rules(initial_config, points):
    rule = "par"
    #first rule
    matrix = _generate_matrix(initial_config)
    print(matrix)
    if len(initial_config) %2 == 0:
        print("Tabuleiro de tamanho par")
        #second rule
        if initial_config.index(0) %2 != 0: #TODO: get intercalate row
            #solução impar
            rule = "impar"
        else:
            #third rule
            rule = "par"
    else:
        print("Tabuleiro de tamanho impar")
        
    if rule == "par":
        return False if points % 2 == 0 else True
    if rule =="impar":
        return True if points % 2 == 0 else False        


def there_is_no_solution(initial_config, final_config):
    points  = 0
    for i, value in enumerate(initial_config):
        if final_config[i] == 0:
            points += 0
        else:
            points += len([x for x in initial_config[i:] if x < value and x != 0])
            print(f"Position={i} |Pontos = {points} | inversões = {len([i for i in initial_config[value:] if i > value])}")

    print(points)
    return _solubility_rules(initial_config, points)

def _generate_matrix(array):
    matrix = []
    count = 0
    aux = []
    for p, i in enumerate(array):
        if count < matrix_width:
            aux.append(i)
            count += 1
            if p+1 == len(initial_config):
                matrix.append(aux[:])
        else:
            matrix.append(aux[:])
            aux = []
            aux.append(i)
            count = 1
    return matrix

def init_game():
    if there_is_no_solution(final_config, initial_config):
        print("Não há solução")
    else:
        print("Encontrei uma solução :)")
    

if __name__ == "__main__":
    assert len(initial_config) == len(final_config), "Os tabuleiros devem possuir o mesmo tamanho."
    
    init_game()

