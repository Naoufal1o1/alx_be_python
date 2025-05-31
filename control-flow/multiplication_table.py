# multiplication_table.py

def generate_table():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Please enter a valid integer.")

# Run the function
if __name__ == "__main__":
    generate_table()
