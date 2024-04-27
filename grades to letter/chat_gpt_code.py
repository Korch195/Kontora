def calculate_grade(grade1, grade2, grade3, grade4, grade5):
    # Checking if grades are within the valid range
    if not (0 <= grade1 <= 100 and 0 <= grade2 <= 100 and 0 <= grade3 <= 100 
            and 0 <= grade4 <= 100 and 0 <= grade5 <= 100):
        return None
    
    # Calculating the average grade
    average_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
    
    # Assigning letter grade based on the average
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
    
    return round(average_grade, 1), letter_grade

if __name__ == "__main__":
    grade1 = int(input())
    grade2 = int(input())
    grade3 = int(input())
    grade4 = int(input())
    grade5 = int(input())
    
    result = calculate_grade(grade1, grade2, grade3, grade4, grade5)
    
    if result:
        percent_grade, letter_grade = result
        print(f"Average grade = {percent_grade} -> {letter_grade}")
    else:
        print("None")
