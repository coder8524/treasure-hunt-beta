import random

main_grid = []
def grid():
    for i in range(5):
        row = []
        for j in range(5):
            row.append("-")
        main_grid.append(row)
    return main_grid
            
e = grid()
print(e)
