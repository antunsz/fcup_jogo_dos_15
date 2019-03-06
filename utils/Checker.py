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
                print("Position={} |Pontos = {} | inversões = {}".format(i, self.puzzle.points, len([i for i in self.puzzle.initial_config[value:] if i > value])))

        return self._solubility_rules()