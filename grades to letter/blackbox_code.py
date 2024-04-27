def calculate_grades(grades: tuple) -> tuple[float | None, str | None]:
    if not grades:
        return None, None

    total_grade = 0
    valid_grades = all(g >= 0 and g <= 100 for g in grades)

    if valid_grades:
        for grade in grades:
            total_grade += grade
        average_grade = round(total_grade / len(grades), 1)

        if 90 <= average_grade <= 100:
            letter_grade = 'A'
        elif 80 <= average_grade < 90:
            letter_grade = 'B'
        elif 75 <= average_grade < 80:
            letter_grade = 'C'
        elif 65 <= average_grade < 75:
            letter_grade = 'D'
        elif 60 <= average_grade < 65:
            letter_grade = 'E'
        else:
            letter_grade = 'F'
    else:
        average_grade = None
        letter_grade = None

    return average_grade, letter_grade