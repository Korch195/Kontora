class PolishOrderingError(Exception):
    pass

def ordering_beers(number):
        if not 0 <= number <= 99:
            raise PolishOrderingError("Number of beers must be between 0 and 99.")
        
        if number == 0:
            return "Woda mineralna poprosze"
        
        units = number % 10
        tens = number // 10
        nominative_plural = "piwa"
        genitive_plural = "piw"
        singular = "piwo"
        
        if number == 1:
            beer = singular
            numeral = "Jedno"
        elif units == 1 and tens != 1:
            beer = singular
            numeral = f"{number}"
        elif units in [2, 3, 4] and tens != 1:
            beer = nominative_plural
            numeral = f"{number}"
        else:
            beer = genitive_plural
            numeral = f"{number}"
        
        if number in [12, 13, 14]:
            beer = genitive_plural
        
        numbers = {
            0: "zero", 1: "jedno", 2: "dwa", 3: "trzy", 4: "cztery", 5: "piec",
            6: "szesc", 7: "siedem", 8: "osiem", 9: "dziewiec", 10: "dziesiec",
            11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie",
            15: "pietnascie", 16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie",
            19: "dziewietnascie", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci",
            50: "piecdziesiat", 60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat",
            90: "dziewiecdziesiat"
        }
        
        if number in numbers:
            numeral = numbers[number]
        elif tens == 0:
            numeral = numbers[units]
        else:
            numeral = f"{numbers[tens*10]} {numbers[units]}"
        
        return f"{numeral.capitalize()} {beer} poprosze"