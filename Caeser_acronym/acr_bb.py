def create_acronym(message):
    # Check if the message is a string and contains newline characters
    if not isinstance(message, str):
        return None
    if not message:
        return None
    # Split the message into phrases
    phrases = message.split('\n')
    
    # Check if the last phrase does not end with an empty line
    if phrases[-1] == '':
        phrases = phrases[:-1]
    
    # my intervention
    phrases_copy = [phrase.replace("'", "") for phrase in phrases]
    # Check if all phrases consist of only letters
    if not all(phrase.replace(" ", "").isalpha() for phrase in phrases_copy):
        return None
    
    # Create acronyms for each phrase
    acronyms = []
    for phrase in phrases:
        words = phrase.split()
        acronym = ''.join(word[0].upper() for word in words)
        acronyms.append(f"{acronym} - {phrase}")
    
    return '\n'.join(acronyms)