#Oxt4n1nc9b4r


import random

def print_board(cat_position, mouse_position):
    for i in range(5):
        for j in range(5):
            if (i, j) == cat_position:
                print("C", end=" ")  # Cat
            elif (i, j) == mouse_position:
                print("M", end=" ")  # Mouse
            else:
                print(".", end=" ")  # Empty space
        print()

def move_entity(entity_position, direction):
    x, y = entity_position
    if direction == "up":
        return max(x - 1, 0), y
    elif direction == "down":
        return min(x + 1, 4), y
    elif direction == "left":
        return x, max(y - 1, 0)
    elif direction == "right":
        return x, min(y + 1, 4)

def play_game():
    cat_position = (random.randint(0, 4), random.randint(0, 4))
    mouse_position = (random.randint(0, 4), random.randint(0, 4))

    while True:
        print_board(cat_position, mouse_position)

        direction = input("Enter direction (up/down/left/right): ").lower()

        cat_position = move_entity(cat_position, direction)
        mouse_position = move_entity(mouse_position, random.choice(["up", "down", "left", "right"]))

        if cat_position == mouse_position:
            print("Game Over! The cat caught the mouse.")
            break

if __name__ == "__main__":
    play_game()
