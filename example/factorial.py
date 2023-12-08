def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n)

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

number = get_integer_input("Enter a number to calculate its factorial: ")
result = factorial(number)
print(f"The factorial of {number} is {result}")
