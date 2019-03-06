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