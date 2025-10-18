def find_maximum_number_in_array(numbers):
    maximum_number = float('-inf')
    for i in numbers:
        if i > maximum_number:
            maximum_number = i
    
    return maximum_number