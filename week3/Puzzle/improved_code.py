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


def check_colour(board):
    """
    the function checks if each block of cells of the same color must contain \
digits without repetition

    >>> check_colour( [\
     "**** ****",\
     "***1 ****",\
     "**  3****",\
     "* 4  ****",\
     "     9 53",\
     " 6  83  *",\
     "3   1  **",\
     "  8  2***",\
     "  2  ****"\
     ])
    False
    """

    color_block=[[], [], [], [], []]

    board_column=["", "", "", "", "", "", "", "", ""]

    for element in board:
        for index, _ in enumerate(board_column):
            board_column[index]+=element[index]

    for i in range(5):
        space=board_column[i]
        for sq in space[4-i:]:
            if len(color_block[i])<5:
                color_block[i].append(sq)

    for i in range(5):
        space=board[i+4]
        count_l=0
        for sq in space[::-1]:
            if sq!='*' and count_l<4:
                color_block[4-i].append(sq)
                count_l+=1
                if color_block[4-i].count(sq)>1 and sq.isdigit() or sq==0:
                    return False
    return True
