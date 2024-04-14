def is_pangram(sentence):
    sentence = sentence.lower()
    letters = set()
    for char in sentence:
        if char.isalpha():
            letters.add(char)
    return len(letters) == 26