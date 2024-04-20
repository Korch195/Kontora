#РОБОЧИЙ КОД(ОПТИМІЗАЦІЯ ЗРАЗУ ЦІЛОГО КОДУ)
# import time
# start_time = time.time()

def read_file(file_path):
    """
    Function creates a dictionary, that contains keys - names, surnames and values - iq points \
    by using information from file.
    >>> read_file("smart_people.txt")
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        iq_dict = {}
        for line in file:
            if not line.startswith("#"):
                name, iq = line.strip().split(',')
                iq_dict[name] = int(iq)
        return iq_dict

def rescue_people(smarties: dict, limit_iq):
    """
    Function creates a tuple of the number of trips required and a list of lists, where \
    each inner list represents a trip and contains the names of the people being transported \
    in the order of their selection by the aliens.
    >>> rescue_people({'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, \
'Marilyn vos Savant': 186,'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, \
"Conan O'Brien": 160, 'Emma Watson': 132, 'Barack Obama': 137}, 500)
    (4, [['Marilyn vos Savant', 'Judith Polgar', 'Barack Obama'], ['Elon Musk', \
'Quentin Tarantino', 'Bill Gates'], ["Conan O'Brien", 'Will Smith', 'Mark Zuckerberg'], \
['Emma Watson']])
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({"Alice": 100, "Bob": 80, "Charlie": 90}, 180)
    (2, [['Alice', 'Bob'], ['Charlie']])
    """
    sorted_smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
    total_groups = []
    while sorted_smarties:
        group = []
        total_iq = 0

        for person, iq in sorted_smarties[:]:
            if total_iq + iq <= limit_iq:
                group.append(person)
                total_iq += iq
                sorted_smarties.remove((person, iq))

        total_groups.append(group)

    return len(total_groups), total_groups
# end_time = time.time()
# execution_time = end_time - start_time
# print("Час виконання: ", execution_time, " секунд")

#ОПТИМІЗОВАНА Ф-ІЯ READ_FILE

# def read_file(file_path):
#     """
#     Function creates a dictionary, that contains keys - names, surnames and values - iq points \
#     by using information from file.
#     >>> read_file("smart_people.txt")
#     {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
# 'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
# 'Emma Watson': 132, 'Barack Obama': 137}
#     """
#     with open(file_path, 'r', encoding="utf-8") as file:
#         return {line.split(',')[0]: int(line.split(',')[1]) \
# for line in file if not line.startswith("#")}


# спроба оптимізувати по частинах,але все-таки це НЕ РОБОЧИЙ КОД!!!

# def rescue_people(smarties: dict, limit_iq):
#     """
#     Function creates a tuple of the number of trips required and a list of lists, where \
#     each inner list represents a trip and contains the names of the people being transported \
#     in the order of their selection by the aliens.
#     >>> rescue_people({'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, \
# 'Marilyn vos Savant': 186,'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, \
# "Conan O'Brien": 160, 'Emma Watson': 132, 'Barack Obama': 137}, 500)
#     (4, [['Marilyn vos Savant', 'Judith Polgar', 'Barack Obama'], ['Elon Musk', \
# 'Quentin Tarantino', 'Bill Gates'], ["Conan O'Brien", 'Will Smith', 'Mark Zuckerberg'], \
# ['Emma Watson']])
#     >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
# "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
#     (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
#     >>> rescue_people({"Alice": 100, "Bob": 80, "Charlie": 90}, 180)
#     (2, [['Alice', 'Bob'], ['Charlie']])
#     """
#     sorted_smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
#     total_groups = []
    
#     current_group = []
#     current_iq = 0

#     for person, iq in sorted_smarties:
#         if current_iq + iq <= limit_iq:
#             current_group.append(person)
#             current_iq += iq
#         else:
#             total_groups.append(current_group)
#             current_group = [person]  # Start a new group with the current person
#             current_iq = iq

#     if current_group:  # Add the remaining group
#         total_groups.append(current_group)

#     return len(total_groups), total_groups

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
