def ordering_beers(n):
    if n < 0 or n > 99:
        raise ValueError("Number must be between 0 and 99")
        
    if n == 0:
        return "Woda mineralna poprosze"

    if n == 1:
        return 'Jedno piwo poprosze'    

    units = ["", "jeden", "dwa", "trzy", "cztery", "piec", "szesc" , "siedem", "osiem", "dziewiec", "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
    tens  = ["", "", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

        
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
        return f"{units[n].capitalize()} {plural_genitive} poprosze"
    elif 4<n<20 and n not in exceptions: 
        return f"{units[n].capitalize()} piw poprosze"
    elif 2 <= units_place <= 4 and n not in exceptions:
        return (f"{tens[tens_place].capitalize()} " if tens_place!=0 else '')+(f"{units[units_place].capitalize()} " if tens_place==0 else f"{units[units_place]} ") + f"{plural_nominative} poprosze"
    elif tens_place and units_place==0:
        return f"{tens[tens_place].capitalize()} {plural_genitive} poprosze"
    else:
        return f"{tens[tens_place].capitalize()} {units[units_place]} {plural_genitive} poprosze"
    