def create_acronym(message: str) -> str:
    '''
    str -> str
    takes a string consisting of phrases separated
    by a newline character as an argument, and
    returns the acronyms for these phrases
    >>> print(create_acronym("random access memory"))
    RAM - random access memory
    >>> print(create_acronym("random 123"))
    None
    '''
    if not isinstance(message, str):
        return None
    result = ''
    message = message.split('\n')
    for i in message:
        for j in i:
            if j.isdigit():
                return None
        string = ''
        sentence = i.split()
        for j in sentence:
            if j:
                string += j[0].upper()
        if string:
            result += f'{string} - {i}\n'
    return result.strip()

def caesar_encode(message, key):
    '''
    (str, int) -> str
    turns the string into a Caesar encryption
    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    >>> caesar_encode('zyra', 2)
    'batc'
    >>> caesar_encode('cute', 9)
    'ldcn'
    '''
    encoded_message = ''
    for char in message:
        if char == ' ':  # пропускаємо пробіли
            encoded_message += char
            continue
        encoded_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        encoded_message += encoded_char
    return encoded_message


def caesar_decode(message, key):
    '''
    (str, int) -> str
    decrypts Caesar's code and returns the original message
    >>> caesar_decode('frpsxwhu', 3)
    'computer'
    >>> caesar_decode('batc', 2)
    'zyra'
    >>> caesar_decode('ldcn', 9)
    'cute'
    '''
    decoded_message = ''
    for char in message:
        if char == ' ':
            decoded_message += char
            continue
        decoded_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        decoded_message += decoded_char
    return decoded_message