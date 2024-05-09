def is_palindrome_recursive(word, low_index, high_index):
    if not bool(word):
        return False
    low_word = word[low_index]
    high_word = word[high_index]
    if low_index >= high_index:
        return True
    if low_word == high_word:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    elif low_word != high_word:
        return False
