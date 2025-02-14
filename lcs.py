import random

def str2arr(s) -> list:
    return list(s)

def LCS(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1

    l = [[0] * n for _ in range(m)]
    b = [[' '] * n for _ in range(m)]  # Backtracking table

    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1] == s2[j-1]:
                l[i][j] = l[i-1][j-1] + 1
                b[i][j] = "↖"
            elif l[i-1][j] >= l[i][j-1]:
                l[i][j] = l[i-1][j]
                b[i][j] = "↑"
            else:  
                l[i][j] = l[i][j-1]
                b[i][j] = "←"

    return l, b  # Return both LCS and backtracking table

def backtrack_LCS(s1, s2, b):
    i, j = len(s1), len(s2)
    lcs = []
    path = set()

    while i > 0 and j > 0:
        path.add((i, j))  # Store path indices
        if b[i][j] == "↖":
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == "↑":
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs)), path

# Function to generate random colors for numbers
def generate_color_map(matrix):
    max_val = max(max(row) for row in matrix)
    color_map = {0: "\033[97m"}

    for num in range(1, max_val + 1):
        if num not in color_map:
            color_map[num] = f"\033[38;5;{random.randint(1, 255)}m"  

    return color_map

def print_colored_matrix(matrix, b, path, s1, s2):
    color_map = generate_color_map(matrix)
    reset = "\033[0m"
    bold_red = "\033[1;31m"
    bold_blue = "\033[1;34m"

    print("\nLCS Table")
    print("\n   ", end="")
    for c in " " + s2:
        print(f"{bold_blue}{c}{reset}  ", end="")
    print()

    for i in range(len(matrix)):
        if i > 0:
            print(f"{bold_blue}{s1[i-1]}{reset} ", end="")
        else:
            print("  ", end="")

        for j in range(len(matrix[0])):
            color = color_map.get(matrix[i][j], "\033[97m")
            highlight = bold_red if (i, j) in path else ""
            arrow = f"\033[93m{b[i][j]}\033[0m" if b[i][j] != " " else " "
            print(f"{highlight}{color}{matrix[i][j]}{reset}{arrow} ", end="")
        print() 

def print_lcs_path(matrix, b, path, s1, s2):
    reset = "\033[0m"
    bold_red = "\033[1;31m"
    bold_blue = "\033[1;34m"

    print("\n Path Visualization")
    print("\n   ", end="")
    for c in " " + s2:
        print(f"{bold_blue}{c}{reset}  ", end="")
    print()

    for i in range(len(matrix)):
        if i > 0:
            print(f"{bold_blue}{s1[i-1]}{reset} ", end="")
        else:
            print("  ", end="")

        for j in range(len(matrix[0])):
            highlight = bold_red if (i, j) in path else ""
            arrow = f"{bold_red}{b[i][j]}{reset}" if (i, j) in path else b[i][j]
            print(f"{highlight}{matrix[i][j]}{reset}{arrow} ", end="")
        print()

def print_final_LCS(s1, s2, lcs):
    bold_green = "\033[1;32m"
    reset = "\033[0m"

    highlighted_s1 = "".join(f"{bold_green}{c}{reset}" if c in lcs else c for c in s1)
    highlighted_s2 = "".join(f"{bold_green}{c}{reset}" if c in lcs else c for c in s2)

    print("\nMatching String Highlights")
    print(f"String 1: {highlighted_s1}")
    print(f"String 2: {highlighted_s2}")

    print("\n LCS String ")
    print(f"{bold_green}{lcs}{reset}")

print("Enter two strings to find the longest common subsequence:\n")
s1 = input("Enter string #1: ")
s2 = input("Enter string #2: ")

s1_arr = str2arr(s1)
s2_arr = str2arr(s2)

lcs_matrix, backtrack_table = LCS(s1_arr, s2_arr)

lcs_str, lcs_path = backtrack_LCS(s1_arr, s2_arr, backtrack_table)

print_colored_matrix(lcs_matrix, backtrack_table, lcs_path, s1, s2)

print_lcs_path(lcs_matrix, backtrack_table, lcs_path, s1, s2)

print_final_LCS(s1, s2, lcs_str)
