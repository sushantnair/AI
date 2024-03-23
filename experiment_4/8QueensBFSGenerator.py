from collections import deque
import time, psutil

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
cnt = 1
def print_board(board):
    global cnt
    with open('bfs.txt', 'a') as file:
        file.write(f'{cnt}\n')
    with open('bfs_output.txt', 'a') as file:
        file.write(f'{cnt}\n')
    cnt += 1
    n = len(board)
    for i in range(n):
        line = ""
        for j in range(n):
            if j == board[i]:
                line += "Q "
            else:
                line += "_ "
        with open('bfs.txt', 'a') as file:
            file.write(f'{line}')
        with open('bfs_output.txt', 'a') as file:
            file.write(f'{line}\n')
    with open('bfs.txt', 'a') as file:
        file.write('\n')
    with open('bfs_output.txt', 'a') as file:
        file.write('\n')

def bfs(n):
    queue = deque([([-1]*n, 0)])  # Board state and current row
    while queue:
        board, curr_row = queue.popleft()
        
        if curr_row == n:  # If a solution is found
            print_board(board)
            return
        
        for i in range(n):  
            if is_safe(board, curr_row, i):  
                new_board = list(board)  
                new_board[curr_row] = i 
                with open('bfs.txt', 'a') as file:
                    file.write(f"\n{curr_row})\n")
                with open('bfs_output.txt', 'a') as file:
                    file.write(f"\n{curr_row})\n")
                print_board(new_board) 
                queue.append((new_board, curr_row+1))  
    
if __name__ == "__main__":
    print('8 Queens using Breadth First Search')
    process = psutil.Process()

    start_time = time.time()

    bfs(8)

    end_time = time.time()
    execution_time = (end_time - start_time) 

    memory_info = process.memory_info()
    used_memory = memory_info.rss / (1024 ** 2)  # Convert to megabytes

    print(f"\nExecution Time: {execution_time:.4f} s")
    print(f"Memory Used: {used_memory:.2f} MB")
