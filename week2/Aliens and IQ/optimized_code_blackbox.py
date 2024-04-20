#НЕ РОБОЧИЙ КОД,blackbox не зміг оптимізувати
# import time

# def read_file(file_path):
#     """
#     Function creates a dictionary, that contains keys - names, surnames and values - iq points 
#     by using information from file.
#     >>> read_file("smart_people.txt")
#     {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
# 'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
# 'Emma Watson': 132, 'Barack Obama': 137}
#     """
#     iq_dict = {}
#     with open (file_path,'r',encoding="utf-8") as file:
#         for line in file:
#             if line[0] == "#":
#                 continue
#             name, iq = line.strip().split(',')
#             iq_dict[name] = int(iq)
#         return iq_dict



# def rescue_people(smarties:dict, limit_iq):
#     """
#     Function creates a tuple of the number of trips required and a list of lists, where 
#     each inner list represents a trip and contains the names of the people being transported 
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
#     smarties = list(smarties.items())
#     smarties.sort(key=lambda x: x[1], reverse=True)

#     total_groups = []
#     current_group_iq = 0
#     for name, iq in smarties:
#         if current_group_iq + iq <= limit_iq:
#             total_groups[-1].append(name) if total_groups else total_groups.append([name])
#             current_group_iq += iq
#         else:
#             current_group_iq = iq
#             total_groups.append([name])
#     return (len(total_groups), total_groups)



#НЕ РОБОЧИЙ КОД №2,blackbox теж не зміг оптимізувати
# start_time = time.time()
# """ Aliens and IQ """
# def read_file(file_path):
#     """
#     Function creates a dictionary, that contains keys - names, surnames and values - iq points \
#     by using information from file.
#     >>> read_file("smart_people.txt")
#     {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
# 'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
# 'Emma Watson': 132, 'Barack Obama': 137}
#     """
#     iq_dict = {}
#     with open (file_path,'r',encoding="utf-8") as file:
#         for line in file:
#             if line.startswith("#"):
#                 continue
#             name, iq = line.strip().split(',')
#             iq_dict[name] = int(iq)
#         return iq_dict

# print(read_file('smart_people.txt'))
# end_time = time.time()

# execution_time = end_time - start_time
# print("Час виконання: ", execution_time, " секунд")

# def rescue_people(smarties:dict, limit_iq):
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
#     smarties = list(smarties.items())
#     smarties.sort(key=lambda x: x[1], reverse=True)

#     total_groups = []
#     current_group_iq = 0
#     for name, iq in smarties:
#         if current_group_iq + iq <= limit_iq:
#             if total_groups and total_groups[-1]:
#                 total_groups[-1].append(name)
#             else:
#                 total_groups.append([name])
#             current_group_iq += iq
#         else:
#             current_group_iq = iq
#             total_groups.append([name])
#     return (len(total_groups), total_groups)
