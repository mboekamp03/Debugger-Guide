def calculate_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i + 1]
    return total

def find_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average

def main():
    # Define a list of numbers
    numbers = [10, 20, 30, 40, 50]

    # Calculate the sum of the numbers
    sum_of_numbers = calculate_sum(numbers)
    print(f"The sum of the numbers is: {sum_of_numbers}")

    # Calculate the average of the numbers
    average_of_numbers = find_average(numbers)
    print(f"The average of the numbers is: {average_of_numbers}")

# Run the main function
main()