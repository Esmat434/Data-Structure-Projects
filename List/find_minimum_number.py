def find_minimum_number_in_array(numbers):
    minimum_number = float('inf')
    for number in numbers:
        if number < minimum_number:
            minimum_number = number
    
    return minimum_number
