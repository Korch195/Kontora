def ordering_beers(number):
    if number == 0:
        return "Woda mineralna poprosze"
    elif number == 1:
        return "Jedno piwo poprosze"
    elif 2 <= number <= 4:
        return f"Dwa {number} piwa poprosze" if number != 2 else f"Dwa piwa poprosze"
    else:
        return f"{number} piw poprosze" if number % 10 in [2, 3, 4] else f"{number} piwa poprosze"

# Test cases
print(ordering_beers(0))  # Woda mineralna poprosze
print(ordering_beers(1))  # Jedno piwo poprosze
print(ordering_beers(2))  # Dwa piwa poprosze
print(ordering_beers(5))  # Pięć piw poprosze
print(ordering_beers(23)) # Dwadzieścia trzy piwa poprosze

