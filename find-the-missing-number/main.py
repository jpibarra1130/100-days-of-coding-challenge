def find_missing_number(input_array):
    total_elements = len(input_array)
    expected_sum = total_elements * (total_elements + 1) / 2
    actual_sum = 0

    for element in input_array:
        actual_sum = actual_sum + element
    
    return expected_sum - actual_sum

if __name__ == "__main__":
    actual = find_missing_number([3, 0, 1])
    expected = 2
    assert actual == expected, f'Expected missing number is {expected} but got {actual}'

    actual = find_missing_number([3, 2, 1])
    expected = 0
    assert actual == expected, f'Expected missing number is {expected} but got {actual}'

    actual = find_missing_number([1])
    expected = 0
    assert actual == expected, f'Expected missing number is {expected} but got {actual}'

    actual = find_missing_number([1, 0])
    expected = 2
    assert actual == expected, f'Expected missing number is {expected} but got {actual}'
