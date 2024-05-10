def is_anagram(first_string, second_string):
    if not bool(first_string) and not bool(second_string):
        return (first_string, second_string, False)

    first_string_lower = list(first_string.lower())
    second_string_lower = list(second_string.lower())

    merge_sort(first_string_lower)
    merge_sort(second_string_lower)

    if first_string_lower == second_string_lower:
        return (
            "".join(first_string_lower),
            "".join(second_string_lower),
            True,
        )
    else:
        return (
            "".join(first_string_lower),
            "".join(second_string_lower),
            False,
        )


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word[general_index] = right[right_index]
            right_index = right_index + 1
