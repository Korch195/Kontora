import tracemalloc
import time

'''
This module has 2 functions. You can find the set of all keywords used in film and\
get a list of movies that have the largest number of keywords.
'''
from collections import defaultdict

def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    '''
    This function should return the set of all keywords\
     used in the movie film_name. Here, film_keywords is\
     a dictionary obtained with input_from_file, where key\
     is the name of the keyword and value is a list of movie\
     names where this keyword is used. If no such movie_name is\
     found, it should return an empty set.
    
    >>> find_film_keywords({"cars": ["Ford", "The lift","Darwash", "Mustang", "Dodge"],\
'animal':["American cat","Mouse trap","Dodge"], "kitchen": ["The Lift", "Dodge", "Darwash"]\
, "life": ['The Sun', 'Dodge']}, "Dodge") == {'cars', 'kitchen', 'life', 'animal'}
    True
    '''
    if not isinstance(film_keywords, dict) or not isinstance(film_name, str):
        return set()  # Return empty set for invalid input
    return set(keyword for keyword, films in film_keywords.items() if film_name in films)

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    '''
    This function should return a list of movies that have the largest number of keywords. \
    The size of the list is determined by num_of_films\
    (i.e., if num_of_films = 0, then return an empty\
    list, if num_of_films = 3, then return a list of three elements).\
    The function returns a list of tuples, where each tuple is of the \
    form (film_name, number_of_keywords), that is, the name of the movie\
    and the number of keywords, respectively. This list is sorted by the\
    number of keywords, starting with the movie with the largest number. If the number is the same,\
    the movies are displayed in lexicographic order.

    >>> find_films_with_keywords({"cars":["Ford", "The lift", "Darwash", "Mustang", "Dodge"],\
"animal": ["American cat", "Mouse trap", "Dodge"], "kitchen":\
 ["The Lift", "Dodge", "Darwash"], "life": ['The Sun', 'Dodge']}, 9)
    [('Dodge', 4), ('Darwash', 2), ('American cat', 1), ('Ford', 1), \
('Mouse trap', 1), ('Mustang', 1), ('The Lift', 1), ('The Sun', 1), ('The lift', 1)]
    '''
    if not isinstance(film_keywords, dict) or not isinstance(num_of_films, int):
        return []  # Return empty list for invalid input
    
    genre_count = defaultdict(int)  # Using defaultdict to count genres
    for films in film_keywords.values():
        for film in films:
            genre_count[film] += 1

    films = sorted(genre_count.items(), key=lambda x: (-x[1], x[0]))[:num_of_films]
    return films


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    tracemalloc.start()
    find_films_with_keywords({"cars":["Ford", "The lift", "Darwash", "Mustang", "Dodge"],
                           "animal": ["American cat", "Mouse trap", "Dodge"],
                           "kitchen": ["The Lift", "Dodge", "Darwash"],
                           "life": ['The Sun', 'Dodge']}, 9)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    #test 2
    tracemalloc.start()
    film_keywords_3 = {f"film{i}": [f"keyword{j}" for j in range(500)] for i in range(500)}
    find_films_with_keywords(film_keywords_3, 5)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    start_time = time.time()
    # Call the function you want to measure
    find_films_with_keywords({"cars":["Ford", "The lift", "Darwash", "Mustang", "Dodge"],
                            "animal": ["American cat", "Mouse trap", "Dodge"],
                            "kitchen": ["The Lift", "Dodge", "Darwash"],
                            "life": ['The Sun', 'Dodge']}, 9)
    end_time = time.time()

    execution_time = end_time - start_time
    print("Test 1 Execution time:", execution_time, "seconds")

    #test 2
    film_keywords_3 = {f"film{i}": [f"keyword{j}" for j in range(500)] for i in range(500)}
    start_time = time.time()
    find_films_with_keywords(film_keywords_3, 5)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Test 2 Execution time:", execution_time, "seconds")