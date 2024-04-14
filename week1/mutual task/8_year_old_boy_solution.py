def multiples_of_3_or_5(number):
    if number < 0:
        return 0
    
    # Initialize sum
    sum_multiples = 0
    
    # Iterate through all numbers below the given number
    for i in range(number):
        # Check if the number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    
    return sum_multiples