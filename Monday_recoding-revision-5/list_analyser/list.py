def list_analyser(numbers):
    if not numbers:
        return 0
    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for number in numbers:
        if number < smallest:
            smallest = number
        
        if number > largest:
            largest = number
        
        total += number

    average = total / len(numbers)

    return smallest, largest, total, average

numbers = [12, 5, 27, 8, 14]
smallest, largest, total, average = list_analyser(numbers)


print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total}")
print(f"Average: {average}")
