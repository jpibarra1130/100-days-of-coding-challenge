from collections import deque

def square_of_sorted_array(raw_array):

    array_length = len(raw_array)
    first_pointer = 0
    last_pointer = array_length - 1

    result = deque()

    for index in range(array_length):
        first_pointer_value = raw_array[first_pointer]
        last_pointer_value = raw_array[last_pointer]
        
        if abs(first_pointer_value) > abs(last_pointer_value):
            new_value = first_pointer_value * first_pointer_value
            first_pointer = first_pointer + 1
        else:
            new_value = last_pointer_value * last_pointer_value
            last_pointer = last_pointer - 1
        
        result.appendleft(new_value)

    return list(result)


if __name__ == "__main__":
    assert square_of_sorted_array([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert square_of_sorted_array([-7,-3,2,3,11]) == [4,9,9,49,121]
    