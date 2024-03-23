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
    with open('dls_output.txt', 'a') as file:
        file.write(f'{cnt}\n')
    with open('dls.txt', 'a') as file:
        file.write(f'{cnt}\n')
    cnt += 1
    for row in board:
        line = ""
        for col in range(len(board)):
            if col == row:
                line += "Q "
            else:
                line += "_ "
        with open('dls_output.txt', 'a') as file:
            file.write(f'{line.strip()}\n')
        with open('dls.txt', 'a') as file:
            file.write(f'{line.strip()}')
    with open('dls_output.txt', 'a') as file:
        file.write('\n')
    with open('dls.txt', 'a') as file:
        file.write('\n')

def solve_queens_dls(board, row, depth_limit):
    if row == len(board):
        print_board(board)
        return

    if row == depth_limit:
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            with open('dls_output.txt', 'a') as file:
                file.write(f'{row + 1})\n')
            with open('dls.txt', 'a') as file:
                file.write(f'\n{row + 1})\n')
            print_board(board)
            solve_queens_dls(board, row + 1, depth_limit)

if __name__ == "__main__":
    print('8 Queens using Depth Limited Search')
    process = psutil.Process()

    start_time = time.time()

    n = 8
    initial_board = [-1] * n  # Initialize an empty board

    with open('dls_output.txt', 'a') as file:
        file.write("0)")
    with open('dls.txt', 'a') as file:
        file.write("0)")
    print_board(initial_board)

    depth_limit = 8  # Set the depth limit for DLS
    solve_queens_dls(initial_board, 0, depth_limit)

    end_time = time.time()
    execution_time = (end_time - start_time) 

    memory_info = process.memory_info()
    used_memory = memory_info.rss / (1024 ** 2)  # Convert to megabytes

    print(f"\nExecution Time: {execution_time:.4f} s")
    print(f"Memory Used: {used_memory:.2f} MB")