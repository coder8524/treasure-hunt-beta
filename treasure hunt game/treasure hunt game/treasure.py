import random

def create_grid():
    return [["-" for _ in range(5)] for _ in range(5)]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def place_treasure():
    return random.randint(0, 4), random.randint(0, 4)

def get_hint(guess_x, guess_y, treasure_x, treasure_y):
    if guess_x < treasure_x:
        return "Try a higher row."
    elif guess_x > treasure_x:
        return "Try a lower row."
    if guess_y < treasure_y:
        return "Try a higher column."
    elif guess_y > treasure_y:
        return "Try a lower column."
    return "You're very close!"

def play_game():
    grid = create_grid()
    treasure_x, treasure_y = place_treasure()
    attempts = 5
    
    print("Welcome to the Treasure Hunt!")
    print("Find the hidden treasure within 5 attempts.")
    print_grid(grid)
    
    while attempts > 0:
        try:
            x = int(input("Enter row (0-4): "))
            y = int(input("Enter column (0-4): "))
            
            if x == treasure_x and y == treasure_y:
                print("Congratulations! You found the treasure!")
                grid[x][y] = "T"
                print_grid(grid)
                return
            else:
                print("No treasure here!")
                print(get_hint(x, y, treasure_x, treasure_y))
                grid[x][y] = "X"
                attempts -= 1
                print(f"Attempts left: {attempts}")
                print_grid(grid)
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 4.")
    
    print("Game over! You've run out of attempts.")
    print(f"The treasure was at ({treasure_x}, {treasure_y})")
    
play_game()

