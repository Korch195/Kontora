def ordering_beers(n):
    if n < 0 or n > 99:
        raise ValueError("Number must be between 0 and 99")

    units = ["", "jeden", "dwa", "trzy", "cztery", "piec", "szesc" , "siedem", "osiem", "dziewiec", "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
    tens  = ["", "", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]
    
    exceptions = [12, 13, 14]
        
    plural_genitive = "piw"
    plural_nominative = "piwa"
    
    tens_place = n // 10
    units_place = n % 10

    if n == 0:
        return "Woda mineralna poprosze"
    
    if n == 1:
        return 'Jedno piwo poprosze'

    if n in exceptions:
        return f"{units[n].capitalize()} {plural_genitive} poprosze"

    if 4<n<20 and n not in exceptions:
        return f"{units[n].capitalize()} piw poprosze"

    if 2 <= units_place <= 4 and n not in exceptions:
        return (f"{tens[tens_place].capitalize()} " if tens_place!=0 else '')+(f"{units[units_place].capitalize()} " if tens_place==0 else f"{units[units_place]} ") + f"{plural_nominative} poprosze"
    
    if tens_place and units_place==0:
        return f"{tens[tens_place].capitalize()} {plural_genitive} poprosze"
    
    return f"{tens[tens_place].capitalize()} {units[units_place]} {plural_genitive} poprosze"
    