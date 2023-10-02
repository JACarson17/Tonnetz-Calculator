from triad import Triad
from typing import Optional

class Node():
    def __init__(self, traid: Triad) -> None:
        self.triad = traid
        self.end = False
        self.l_leg = None
        self.p_leg = None
        self.r_leg = None

class Tree():
    def __init__(self, root: Triad, target: Triad) -> None:
        self.root = Node(root)
        self.target = target

    def insert(self, root: Node, position):
        if position == 'r':
            transform = Node(root.triad.r_transform())
            root.r_leg = transform
        elif position == 'p':
            transform = Node(root.triad.p_transform())
            root.p_leg = transform
        elif position == 'l':
            transform = Node(root.triad.l_transform())
            root.l_leg = transform
        
        if transform.triad.name == self.target.name:
            transform.end = True
            return True, transform
        else:
            return False, transform
    
    def build(self):
        solved = False
        to_search = [self.root]
        while not solved:
            search = to_search.pop(0)
            for transform in ['r', 'p', 'l']:
                solved, new = self.insert(search, transform)
                to_search.append(new)
                if solved:
                    break

    def traverse(self, root: Node, searched: Optional[list[Node]] = None):
        legs: list[Node] = [l for l in [root.l_leg, root.p_leg, root.r_leg] if l is not None]
        
        for leg in legs:
            if leg.end:
                return [leg]
            else:
                found = self.traverse(leg, searched)
                if found is not None:
                    return [leg] + found


def print_solution(solution: list[Node]):
    to_print = []
    for node in solution:
        to_print.append(node.triad.name)
        to_print.append([node.triad.root.name, node.triad.third.name, node.triad.fifth.name])
        to_print.append('')
    for line in to_print:
        print(line)

if __name__ == '__main__':
    start = Triad('C')
    target = Triad('B', False)
    solver = Tree(start, target)
    solver.build()
    solution = [solver.root] + solver.traverse(solver.root)
    print_solution(solution)