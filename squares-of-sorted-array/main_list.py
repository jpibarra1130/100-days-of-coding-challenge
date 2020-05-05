# using list
def square_of_sorted(raw_array):

    array_length = len(raw_array)
    first_pointer = 0
    last_pointer = array_length - 1

    result = [None] * array_length

    # range isn't inclusive
    for index in range(1, array_length + 1):
        first_pointer_value = raw_array[first_pointer]
        last_pointer_value = raw_array[last_pointer]
        
        if abs(first_pointer_value) > abs(last_pointer_value):
            new_value = first_pointer_value * first_pointer_value
            first_pointer = first_pointer + 1
        else:
            new_value = last_pointer_value * last_pointer_value
            last_pointer = last_pointer - 1
        
        result[index * -1] = new_value
    
    return result

if __name__ == "__main__":
    assert square_of_sorted([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert square_of_sorted([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert square_of_sorted([4]) == [16]
