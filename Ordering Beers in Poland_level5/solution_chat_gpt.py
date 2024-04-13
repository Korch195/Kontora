class Translator:
    @staticmethod
    def ordering_beers(n):
        if n < 0 or n > 99:
            raise ValueError("Number must be between 0 and 99")
        
        if n == 0:
            return "Woda mineralna poprosze"
        
        units = ["", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
        teens = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie",
                 "siedemnascie", "osiemnascie", "dziewietnascie"]
        tens = ["", "dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat",
                "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]
        
        plural_genitive = "piw"
        plural_nominative = "piwa"
        singular = "piwo"
        
        # Define exceptions for 12, 13, and 14
        exceptions = [12, 13, 14]
        
        # Get the last two digits
        tens_place = n // 10
        units_place = n % 10
        
        # Combine words for two-digit numbers
        if n in exceptions:
            return f"{teens[n-10]} {plural_genitive} poprosze"
        elif 2 <= units_place <= 4 and n not in exceptions:
            return f"{tens[tens_place]} {units[units_place]} {plural_nominative} poprosze"
        elif units_place == 1 and n not in exceptions:
            return f"Jedno {singular} poprosze"
        elif tens_place == 2 or tens_place == 3 or tens_place == 4:
            return f"{tens[tens_place]} {units[units_place]} {plural_nominative} poprosze"
        else:
            return f"{tens[tens_place]} {units[units_place]} {plural_nominative} poprosze"

# Test cases
print(Translator.ordering_beers(1))   # Jedno piwo poprosze
print(Translator.ordering_beers(2))   # Dwa piwa poprosze
print(Translator.ordering_beers(12))  # 12 piw poprosze
print(Translator.ordering_beers(22))  # 22 piwa poprosze
print(Translator.ordering_beers(23))  # 23 piwa poprosze
print(Translator.ordering_beers(57))   # Piecdziesiat siedem piwa poprosze
print(Translator.ordering_beers(0))   # Woda mineralna poprosze
