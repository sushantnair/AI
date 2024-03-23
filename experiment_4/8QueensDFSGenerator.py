import time, psutil

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
cnt = 1
def print_board(board):
    global cnt
    with open('dfs_output.txt', 'a') as file:
        file.write(f'Board Count: {cnt}\n')
    with open('dfs.txt', 'a') as file:
        file.write(f'Board Count: {cnt}\n')
    cnt+=1
    for row in board:
        line = ""
        for col in range(len(board)):
            if col == row:
                line += "Q "
            else:
                line += "_ "
        with open('dfs_output.txt', 'a') as file:
            file.write(f'{line.strip()}\n')
        with open('dfs.txt', 'a') as file:
            file.write(f'{line.strip()}')
    with open('dfs_output.txt', 'a') as file:
        file.write('\n')
    with open('dfs.txt', 'a') as file:
        file.write('\n')

def solve_queens(board, row):
    if row == len(board):
        print_board(board)
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            with open('dfs_output.txt', 'a') as file:
                file.write(f"{row + 1})\n")
            with open('dfs.txt', 'a') as file:
                file.write(f"\n{row + 1})\n")
            print_board(board)
            solve_queens(board, row + 1)

if __name__ == "__main__":
    print('8 Queens using Depth First Search')
    process = psutil.Process()

    start_time = time.time()

    n = 8
    initial_board = [-1] * n  # Initialize an empty board
    with open('dfs_output.txt', 'a') as file:
        file.write("0)\n")
    with open('dfs.txt', 'a') as file:
        file.write("0)\n")
    print_board(initial_board)

    solve_queens(initial_board, 0)

    end_time = time.time()
    execution_time = (end_time - start_time) 

    memory_info = process.memory_info()
    used_memory = memory_info.rss / (1024 ** 2)  # Convert to megabytes

    print(f"\nExecution Time: {execution_time:.4f} s")
    print(f"Memory Used: {used_memory:.2f} MB")
    
