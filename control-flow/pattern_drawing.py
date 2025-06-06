# pattern_drawing.py

def draw_pattern():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return

        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # move to next line after each row
            row += 1

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Run the function
if __name__ == "__main__":
    draw_pattern()
