from collections import deque

def create_new_sequence(sequence):
    new_sequence = ""
    queue = deque(sequence)
    counter = 0

    while queue:
        current_character = queue.popleft()
        next_character = queue[0] if len(queue) > 0 else None

        if current_character == next_character:
            counter += 1
        else:
            counter += 1
            new_sequence += f"{counter}{current_character}"
            counter = 0

    return new_sequence


def look_and_say(n):
    sequence = "1"
    counter = 1
    while (counter < n ):
        sequence = create_new_sequence(sequence)
        counter += 1

    return sequence

if __name__ == "__main__":

    # test getting the new sequence
    actual = create_new_sequence("1")
    expected = "11"
    assert actual == expected, f'Expected is {expected} but actual is {actual}'

    actual = create_new_sequence("11")
    expected = "21"
    assert actual == expected, f'Expected is {expected} but actual is {actual}'

    actual = create_new_sequence("31131211131221")
    expected = "13211311123113112211"
    assert actual == expected, f'Expected is {expected} but actual is {actual}'

    # Actual look and say
    actual = look_and_say(1)
    expected = "1"
    assert actual == expected, f'Expected is {expected} but actual is {actual}'

    actual = look_and_say(2)
    expected = "11"
    assert actual == expected, f'Expected is {expected} but actual is {actual}'

    actual = look_and_say(9)
    expected = "31131211131221"
    assert actual == expected, f'Expected is {expected} but actual is {actual}'