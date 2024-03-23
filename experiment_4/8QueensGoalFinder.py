# BFS: Q _ _ _ _ _ _ _ _ _ _ _ Q _ _ _ _ _ _ _ _ _ _ Q _ _ _ _ _ Q _ _ _ _ Q _ _ _ _ _ _ _ _ _ _ _ Q _ _ Q _ _ _ _ _ _ _ _ _ Q _ _ _ _
# DFS/DLS: Q _ _ _ _ _ _ __ _ _ _ Q _ _ __ _ _ _ _ _ _ Q_ _ _ _ _ Q _ __ _ Q _ _ _ _ __ _ _ _ _ _ Q __ Q _ _ _ _ _ __ _ _ Q _ _ _ _

import time, psutil

def search_in_file(file_path, search_line):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # Print the current line (without newline characters)
                if line.strip() == search_line:
                    print("Match found! Exiting.")
                    break
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = 'dls.txt'
    print(f'Searching in: {file_path}')

    search_line = 'Q _ _ _ _ _ _ __ _ _ _ Q _ _ __ _ _ _ _ _ _ Q_ _ _ _ _ Q _ __ _ Q _ _ _ _ __ _ _ _ _ _ Q __ Q _ _ _ _ _ __ _ _ Q _ _ _ _'

    process = psutil.Process()

    start_time = time.time()

    search_in_file(file_path, search_line)

    end_time = time.time()
    execution_time = (end_time - start_time) 

    memory_info = process.memory_info()
    used_memory = memory_info.rss / (1024 ** 2)  # Convert to megabytes

    print(f"\nExecution Time: {execution_time:.4f} s")
    print(f"Memory Used: {used_memory:.2f} MB")



