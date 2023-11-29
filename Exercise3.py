def unique_chars_list(input_list):
    new_list = []

    for string in input_list:
        unique_chars = ''.join(sorted(set(string), key=string.index))
        new_list.append(unique_chars)

    return new_list


input_strings = ["hello", "world", "python"]
result = unique_chars_list(input_strings)
print(result)