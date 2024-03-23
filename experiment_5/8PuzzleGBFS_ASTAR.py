import numpy as np
from tabulate import tabulate as t

def print_puzzle(puzzle):
    print(t(puzzle, tablefmt='grid'))

def compare(goal, board):
    h = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if goal[i][j] != board[i][j]:
                h += 1 
    return h

def blank_pos(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == -1:
                return i, j
            
def next_move(board):
    row, col = blank_pos(board)
    moves = []
    # Check if upper box is empty
    if row > 0:
        moves.append((-1, 0))
    # Check if lower box is empty
    if row < len(board) - 1:
        moves.append((1, 0))
    # Check if left box is empty
    if col > 0:
        moves.append((0, -1))
    # Check if right box is empty
    if col < len(board) - 1:
        moves.append((0, 1))
    return moves

def next_state(board):
    s_state = []
    moves = next_move(board)
    row, col = blank_pos(board)
    for move in moves:
        new_state = board.copy()
        new_row = row + move[0]
        new_col = col + move[1]

        #Swap the empty tile with the adjacent tile
        new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
        s_state.append(new_state)
    return s_state

sn = 2
flag = True
def run(s_state_prev_lvl, boards_dict, goal, g):
    global sn
    global flag
    h = 0
    s_state_cur_lvl = list()
    for s_state in s_state_prev_lvl:
        boards = next_state(s_state)
        for board in boards:
            if board.tobytes() not in boards_dict:
                h = compare(goal, board)
                boards_dict[board.tobytes()] = {"g": g, "h": h, "i": g + h}
                s_state_cur_lvl.append(board)
                print('Board Number', sn)
                sn += 1
                print_puzzle(board)
                board_data = boards_dict[board.tobytes()]
                print(board_data)
        if h == 0:
            print('Goal State Found Successfully.')
            flag = False
            search(boards_dict)
            break
    return s_state_cur_lvl

def main():
    '''init = []
    print('Enter the initial state: ')
    for i in range(0, 3):
        row = list()
        for j in range(0, 3):
            num = input('Enter tile value (hit -1 key for blank tile): ')
            row.append(num)
        init.append(row)
    init = np.array(init)
    print('Initial State is\n', init)
    goal = []
    print('Enter the goal state: ')
    for i in range(0, 3):
        row = list()
        for j in range(0, 3):
            num = input('Enter tile value (hit -1 key for blank tile): ')
            row.append(num)
        goal.append(row)
    goal = np.array(goal)
    print('Goal State is\n', goal)'''
    init = np.array([[1, 2, 3],
                    [-1, 4, 6],
                    [7, 5, 8]])
    goal = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, -1]])
    
    boards_dict = dict()
    print('Initial State')
    print_puzzle(init)
    print('Goal State')
    print_puzzle(goal)

    # Steps

    sn = 1
    print('Level 0')
    g = 0
    h = compare(goal, init)
    boards_dict[init.tobytes()] = {"g": g, "h": h, "i": g + h}
    print('Board Number', sn)
    print_puzzle(init)
    board_data = boards_dict[init.tobytes()]
    print(board_data)

    num_levels = 50

    # As you can see above, for each level I'm hard-coding. But what to do if there are 50 levels?
    # Creating a list to store s_state_l0, s_state_l1, ...
    s_states = [list() for _ in range(num_levels)]
    for level in range(0, num_levels):
        if flag == True:
            if level == 0:
                s_states[level].append(init)
            else:
                print(f'Level {level}')
                s_states[level] = run(s_state_prev_lvl = s_states[level - 1], boards_dict = boards_dict, goal = goal, g = level)
        else:
            break

def search(boards_dict):
    print('Now that the mapping of boards with their \'g\', \'h\' and \'i\', the searching can begin.')
    astar(boards_dict)
    gbfs(boards_dict)

def astar(boards_dict):
    print('A* Informed Search Algorithm')
    solution_path = list()
    for key, value in boards_dict.items():
        board = np.frombuffer(key, dtype=int).reshape(3,3)
        if all(value['i'] <= boards_dict[k]['i'] for k, v in boards_dict.items() if v['g'] == 2):
            solution_path.append(board)
    for solution in solution_path:
        print_puzzle(solution)

def gbfs(boards_dict):
    print('Greedy Best First Search Algorithm')
    solution_path = list()
    min_h = 10
    for key, value in boards_dict.items():
        # board = np.frombuffer(key, dtype=int).reshape(3,3)
        for i in range(0,4):
            if value['g'] == i:
                # print_puzzle(board)
                if value['h'] < min_h:
                    min_h = value['h']
                    solution_path.append(key)
    for selected_board in solution_path:
        board = np.frombuffer(selected_board, dtype=int).reshape(3,3)
        print_puzzle(board)

if __name__ == "__main__":
    main()        
