def sum_of_digits(number: int):
    print(number)
    if not isinstance(number, int):
        raise ValueError
    number = abs(number)
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result
# hey

def is_lucky(number: int):
    if not isinstance(number, int):
        raise ValueError
    number = abs(number)
    if number < 10:
        return True
    head = sum_of_digits(number // 10 ** ((len(str(number)) + 1) // 2))
    tail = sum_of_digits(number % 10 ** (len(str(number)) // 2))
    if head == tail:
        return True
    return False


print("ok")
print(sum_of_digits(123))
