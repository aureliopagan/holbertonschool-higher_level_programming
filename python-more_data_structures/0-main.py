# 0-main.py

#!/usr/bin/python3
from 0-square_matrix_simple import square_matrix

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = square_matrix(matrix)
    print("Square matrix result:")
    print(result)

if __name__ == "__main__":
    main()