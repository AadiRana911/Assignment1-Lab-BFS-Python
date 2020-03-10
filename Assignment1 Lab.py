class Node:
    def __init__(self, state, parent, actions):
        self.state = state
        self.parent = parent
        self.actions = actions

graph = {
         'A': Node('A', None, ['B','Y']),
         'B': Node('B', None, ['A','C']),
         'C': Node('C', None, ['B','D']),
         'D': Node('D', None, ['E','C']),
         'E': Node('E', None, ['F','D']),
         'F': Node('F', None, ['G','E']),
         'G': Node('G', None, ['H','F']),
         'H': Node('H', None, ['I','L','G']),
         'I': Node('I', None, ['J','H']),
         'J': Node('J', None, ['K','I']),
         'K': Node('K', None, ['J']),
         'L': Node('L', None, ['M','H']),
         'M': Node('M', None, ['N','P','L']),
         'N': Node('N', None, ['O','M']),
         'O': Node('O', None, ['P','N','Q']),
         'P': Node('P', None, ['M','O']),
         'Q': Node('Q', None, ['R','O']),
         'R': Node('R', None, ['S','T','Q']),
         'S': Node('S', None, ['R']),
         'T': Node('T', None, ['U','R']),
         'U': Node('U', None, ['T','V']),
         'V': Node('V', None, ['W','Z','U']),
         'W': Node('W', None, ['X','V']),
         'X': Node('X', None, ['Y','W']),
         'Y': Node('Y', None, ['A','X']),
         'Z': Node('Z', None, ['V'])
         }

def bfs(g, initialstate, goalstate):
    frontier = {initialstate}
    explored = set()
    while len(frontier) != 0:
        currentNode = frontier.pop()
        explored.add(currentNode)
        for child in g[currentNode].actions:
            if child not in frontier and child not in explored:
                g[child].parent = currentNode
                if g[child].state == goalstate:
                    return actionSequence(g, initialstate, goalstate)
                frontier.add(child)

def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

# initialstate = input("Enter your initial state of graph: ")
# goalstate = input("Enter your goal state of graph: ")

initialstate = 'K'
goalstate = 'Z'

if initialstate.capitalize() in graph.keys():
    if goalstate.capitalize() in graph.keys():
        solution = bfs(graph, initialstate.capitalize(), goalstate.capitalize())
        for i in solution:
            print(i , end='')
            if i != solution[-1]:
                print(" -> ", end='')
    else:
        print("Wrong goal state")
else:
    print("Wrong initial state")
 