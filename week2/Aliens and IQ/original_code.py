""" Aliens and IQ """
def read_file(file_path):
    """
    Function creates a dictionary, that contains keys - names, surnames and values - iq points \
    by using information from file.
    >>> read_file("smart_people.txt")
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}
    """
    with open (file_path,'r',encoding="utf-8") as file:
        lines = file.readlines()
        iq_dict = {}
        for line in lines:
            if line[0] == "#":
                continue
            splitted_file = line.split(',')
            iq_dict[splitted_file[0]] = int(splitted_file[1])
        return iq_dict

def rescue_people(smarties:dict, limit_iq):
    """
    Function createsa tuple of the number of trips required and a list of lists, where \
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
    smarties = list(smarties.items())
    smarties.sort(key=lambda x: x[0])
    smarties.sort(key=lambda x: x[1], reverse=True)
    total_groups = []
    while len(smarties) > 0 :
        group = []
        total_iq = 0

        index = 0
        while index < len(smarties):
            person = smarties[index]
            if total_iq + person[1] <= limit_iq:
                group.append(person[0])
                total_iq += person[1]
                smarties.remove(person)
            else:
                index += 1

        total_groups.append(group)

    return (len(total_groups), total_groups)

# end_time = time.time()

# execution_time = end_time - start_time
# print("Час виконання: ", execution_time, " секунд")
