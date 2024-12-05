def group_by(func, seq: list):
    grouped = {}

    for element in seq:
        group_key = func(element)
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(element)

    return grouped



result = group_by(len, ["hi", "dog", "me", "bad", "good"])
print(f"group_by(len, [\"hi\", \"dog\", \"me\", \"bad\", \"good\"]) => {result}")
result = group_by(lambda x: 'even' if x % 2 == 0 else 'odd', [1, 2, 3, 4, 5, 6])
print(f"group_by(lambda x: 'even' if x % 2 == 0 else 'odd', [1, 2, 3, 4, 5, 6]) => {result}")
result = group_by(lambda x: x[0], ["apple", "banana", "avocado", "blueberry", "cherry"])
print(f"group_by(lambda x: x[0], [\"apple\", \"banana\", \"avocado\", \"blueberry\", \"cherry\"]) => {result}")









