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
    if '?' not in expression or 'Скільки' not in expression:
        return 'Неправильний вираз!'
    
    expression = expression.replace('?', '')
    
    try:
        # valid_words = {'додати', 'плюс', 'відняти', 'мінус', 'помножити', 'поділити'}

        if not any(word in expression for word in {'додати', 'плюс', 'відняти', 'мінус', 'помножити', 'поділити'}):
            return 'Неправильний вираз!'
            
        digits = []
        math_operators = []
        res = 0

        for i in expression.split():

            if i == 'додати' or i == 'плюс':
                math_operators.append('+')
            elif i == 'відняти' or i == 'мінус':
                math_operators.append('-')
            elif i == 'помножити':
                math_operators.append('*')
            elif i == 'поділити':
                math_operators.append('/')

            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                digits.append(int(i))
    
            if len(digits) - len(math_operators) >= 2 or len(math_operators) - len(digits) >= 2:
                return 'Неправильний вираз!'

        res = digits[0]
        for op, digit in zip(math_operators, digits[1:]):
            if op == '+':
                res += digit
            elif op == '-':
                res -= digit
            elif op == '*':
                res *= digit
            elif op == '/':
                res /= digit
        return int(res)
    
    except ZeroDivisionError:
        return 'Неправильний вираз!'
    except IndexError:
        return 'Неправильний вираз!'
    


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())