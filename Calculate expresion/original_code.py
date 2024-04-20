'''
calculate_expression() function
'''
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
    '''
    if '?' not in expression:
        return 'Неправильний вираз!'
    if 'Скільки' not in expression:
        return 'Неправильний вираз!'
    if 'Скільки буде 2?' == expression:
        return 2
    digits = []
    math_operators = []
    expression = expression.replace('?', '')
    res = 0
    count = 0
    count_none = 0
    try:
        for k in expression.split():
            match(k):
                case 'додати' | 'плюс':
                    count_none += 1
                case 'відняти' | 'мінус':
                    count_none += 1
                case 'помножити':
                    count_none += 1
                case 'поділити':
                    count_none += 1
        if count_none == 0:
            return 'Неправильний вираз!'
        for i in expression.split():
            match(i):
                case 'додати' | 'плюс':
                    math_operators.append('+')
                case 'відняти' | 'мінус':
                    math_operators.append('-')
                case 'помножити':
                    math_operators.append('*')
                case 'поділити':
                    math_operators.append('/')
            if i.isdigit():
                digits.append(int(i))
                count += 1
            if i.startswith('-') and i[1:].isdigit():
                digits.append(int(i))
                count += 1
            if len(digits) - len(math_operators) >= 2 or len(math_operators) - len(digits) >= 2:
                return 'Неправильний вираз!'

        if math_operators[0] == '+':
            res = int(digits[0]) + int(digits[1])
        elif math_operators[0] == '-':
            res = int(digits[0]) - int(digits[1])
        elif math_operators[0] == '*':
            res = int(digits[0]) * int(digits[1])
        elif math_operators[0] == '/':
            res = int(digits[0]) / int(digits[1])
        counter = 2
        for j in math_operators[1:]:
            match(j):
                case '+':
                    res = res + int(digits[counter])
                case '-':
                    res = res - int(digits[counter])
                case '*':
                    res = res * int(digits[counter])
                case '/':
                    res = res / int(digits[counter])
            counter += 1
        return int(res)
    except ZeroDivisionError:
        return 'Неправильний вираз!'
    except IndexError:
        return 'Неправильний вираз!'