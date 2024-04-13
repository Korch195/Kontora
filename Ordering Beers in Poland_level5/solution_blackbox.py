def ordering_beers(num):
    if num == 0:
        return 'Woda mineralna poprosze'
    elif num == 1:
        return 'Jedno piwo poprosze'
    elif num == 2:
        return 'Dwa piwa poprosze'
    else:
        plural = 'piw' if num % 10 in [2, 3, 4] else 'piwa'
        return f'{num} {plural} poprosze'

print(ordering_beers(0))  # Output: Woda mineralna poprosze
print(ordering_beers(1))  # Output: Jedno piwo poprosze
print(ordering_beers(2))  # Output: Dwa piwa poprosze