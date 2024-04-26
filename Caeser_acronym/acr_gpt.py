import re
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
    phrases = message.strip().split('\n')
    acronyms = []

    for phrase in phrases:
        if not re.match("^[a-zA-Zа-яА-ЯіІїЇ ]+$", phrase):
            return None

        words = phrase.split()
        acronym = ''.join(word[0].upper() for word in words)
        acronyms.append(acronym + " - " + phrase)
    return '\n'.join(acronyms)