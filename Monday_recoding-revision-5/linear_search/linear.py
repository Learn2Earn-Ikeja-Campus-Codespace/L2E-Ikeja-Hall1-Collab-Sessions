values = [14, 7, 22, 9, 7, 31, "a"]
target = 54

def linear_search(values, target):
    for  num in range(len(values)):
        if values[num] == target:
            return (f"Found at index {num}")
        
    return('Target not found')

print(linear_search(values, target))
