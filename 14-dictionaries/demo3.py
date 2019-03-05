words = {
    'a': ['airplane', 'age', 'art'],
    'b': ['banana']
}

word_count_by_letter = {
    key: len(val)
    for key, val in words.items()
}

print(word_count_by_letter)