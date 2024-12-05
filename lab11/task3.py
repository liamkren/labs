from functools import reduce

def filter_using_reduce(condition_func, data_list):
    return reduce(lambda accumulator, item: accumulator + [item] if condition_func(item) else accumulator, data_list, [])

result = filter_using_reduce(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(f"filter_using_reduce(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) => {result}")
result = filter_using_reduce(lambda x: len(x) > 3, ["hi", "dog", "me", "bad", "good"])
print(f"filter_using_reduce(lambda x: len(x) > 3, [\"hi\", \"dog\", \"me\", \"bad\", \"good\"]) => {result}")

