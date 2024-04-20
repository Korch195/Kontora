def calculate_expression(expression: str) -> int:
    '''
    accepts a single argument - a string with a
    simple formulation of a mathematical expression
    and returns an integer - the result of this expression
    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2 2 помножити?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 поділити на 2')
    'Неправильний вираз!'
    >>> calculate_expression('3 плюс 2?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 6 поділити на 0?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2?')
    2
    '''

    if '?' not in expression:
        return 'Неправильний вираз!'
    if 'Скільки' not in expression:
        return 'Неправильний вираз!'
    if len(expression.strip('Скільки буде ')) == 2:
        return int(expression[-2])
    
    expression = expression.replace('?', '')

    digits = []
    math_operators = []
    count = 0
    for i in expression.split():
        if i in ['додати', 'плюс']:
            math_operators.append('+')
        elif i in ['відняти', 'мінус']:
            math_operators.append('-')
        elif i == 'помножити':
            math_operators.append('*')
        elif i == 'поділити':
            math_operators.append('/')
        if i.isdigit():
            digits.append(int(i))
            count += 1
        if i.startswith('-') and i[1:].isdigit():
            digits.append(int(i))
            count += 1
        if len(digits) - len(math_operators) >= 2 or len(math_operators) - len(digits) >= 2:
            return 'Неправильний вираз!'
    
    if len(digits) != len(math_operators) + 1 or len(math_operators) == 0:
        return 'Неправильний вираз!'
    
    res = digits[0]
    for i in range(1, len(digits)):
        if math_operators[i-1] == '+':
            res += digits[i]
        elif math_operators[i-1] == '-':
            res -= digits[i]
        elif math_operators[i-1] == '*':
            res *= digits[i]
        elif math_operators[i-1] == '/':
            if digits[i] == 0:
                return 'Неправильний вираз!'
            res /= digits[i]
    return int(res)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())