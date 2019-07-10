# minegame.py

def main():
    col, row = map(int, input().split())
    matrix = []
    for i in range(row):
        matrix.append(list(input()))
    for x in range(row):
        for y in range(col):
            if matrix[x][y] == '*':
                print(matrix[x][y], sep = '', end ='')
            else:
                count = 0
                for j in range(-1,2):
                    for k in range(-1,2):
                        if 0<=x+j<row and 0<=y+k<col and matrix[x+j][y+k] == '*':
                            count += 1
                print(count, sep ='', end='')
        print()
    
main()
