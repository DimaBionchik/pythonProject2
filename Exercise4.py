def brick(brick_size,hole_size):
    brick_size.sort()
    hole_size.sort()
    for i in range(3):
        if brick_size[i]>hole_size[i]:
            return False
    return True


brick_size = [4,2,4]
hole_size= [3,3,5]
result = brick(brick_size,hole_size)
#print(result)

def unique_characters(strings_list):
    result_list = []
    char_count = {}

    for word in strings_list:


        for char in word:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        uniq_chars = ''.join([char for char, count in char_count.items() if count == 1])
        result_list.append(uniq_chars)

    return result_list


strings_list = ["Hello", "World", "Python"]
result = unique_characters(strings_list)
print(result)


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True



def print_numbers_recursive(A, B):
    if A == B:
        print(A)
    else:
        print(A)
        if A < B:
            print_numbers_recursive(A + 1, B)
        else:
            print_numbers_recursive(A - 1, B)


#A = int(input("Введите число A: "))
#B = int(input("Введите число B: "))

#print(print_numbers_recursive(5,13))


def perimeter(shape, value):
    square_perimeter = 4 * value * (shape == "s")
    circle_perimeter = 2 * 3.14159 * value * (shape == "c")

    return square_perimeter + circle_perimeter



print(perimeter('s',7))
print(perimeter('c',4))
print(perimeter('c',9))
