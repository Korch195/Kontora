"""
Functions check if the logic puzzle playing field is ready to start playing
https://github.com/NastiaKhalus/Khalus-Anastasiia-lab8-task2.git
"""
def validate_board(board: list) -> bool:
    """
    (list) -> bool
    >>> print(validate_board([\
 "**** ****",\
 "***1 ****",\
 "  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  ",\
 "  8  2***",\
 "  2  ****"\
]))
    False
    """
    return check_row(board) and check_column(board) and check_colour(board)

def check_row(board:list) -> bool:
    """
    (list)->bool
    Checks if there two and more identical digits in one row \
    and retuens False if they are present there
    >>> print(check_row(["**** ****",\
 "***1 ****",\
 "  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  ",\
 "  8  2***",\
 "  2  ****"]))
    True

    >>>
    """
    for row in board:
        numbers = []
        for element in row:
            if element.isdigit():
                if element in numbers:
                    return False
                numbers.append(element)
    return True

def check_column(board:list) -> bool:
    """
    (list) -> bool
    Checks if there two and more identical digits in one column \
    and retuens False if they are present there
    >>> print(check_column(["**** ****",\
 "***1 ****",\
 "  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  ",\
 "  8  2***",\
 "  2  ****"]))
    False
    """
    for col in range(9):
        lst = []
        for row in board:
            if row[col].isdigit():
                if row[col] in lst:
                    return False
                lst.append(row[col])
    return True


def check_colour(board:list) -> bool:
    """
    (list) -> bool
    Checks whether coloured filed contains two and more identical digits
    >>> check_colour(["**** ***1",\
"***1 2*",\
"  3*3**",\
"* 4 *4***",\
"    59 7 ",\
" 7 683  *",\
"3 7 1  **",\
" 89  2***",\
"9 2  ****"])
    True
    """
    for row in range(0,9):
        a,b = '',''
        lst = [board[row][8-row]]
        for j in range(row):
            a += board[row][8-j]
            b += board[row - j-1][8 - row]
            if a.isdigit():
                if a in lst:
                    return False
                lst.append(a)
            if b.isdigit():
                if b in lst:
                    return False
                lst.append(b)
    return True