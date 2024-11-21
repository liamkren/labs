def product_of_digits(x):
    x = abs(x)
    if x < 10:
        return x
    return (x % 10) * product_of_digits(x // 10)


def array_to_string(a, index):
    if not a:
        return ""
    if index == len(a) - 1:
        return str(a[index])
    return str(a[index]) + "," + array_to_string(a, index + 1)


def log(base, value):
    if base <= 1 or value <= 0:
        raise ValueError("Base must be > 1 and value must be > 0")
    if value < base:
        return 0
    return 1 + log(base, value // base)


if __name__ == "__main__":
    print(product_of_digits(234))
    print(product_of_digits(-12))
    print(product_of_digits(7))

    print(array_to_string([1, 2, 3, 4], 0))
    print(array_to_string([5], 0))
    print(array_to_string([], 0))

    print(log(10, 123456))
    print(log(2, 64))
    print(log(3, 81))
