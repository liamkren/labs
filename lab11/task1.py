def zipmap(key_list: list, value_list: list, override=False):
    result = {}

    for i, key in enumerate(key_list):
        value = value_list[i] if i < len(value_list) else None

        if key not in result or override:
            result[key] = value

    return result

print(zipmap(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5, 6]))
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))
print(zipmap([1, 2, 3], [4, 5, 6, 7, 8]))
print(zipmap([1, 3, 5, 7], [2, 4, 6]))

