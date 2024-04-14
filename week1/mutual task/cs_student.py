def sum_of_multiples(n):
    if n < 0:
        return 0
    
    # Calculate the sum of multiples of 3
    sum_of_3 = sum(i for i in range(3, n) if i % 3 == 0)
    
    # Calculate the sum of multiples of 5
    sum_of_5 = sum(i for i in range(5, n) if i % 5 == 0)
    
    # Calculate the sum of multiples of 15 (to exclude common multiples)
    sum_of_15 = sum(i for i in range(15, n) if i % 15 == 0)
    
    # Return the sum of multiples of 3 or 5, excluding common multiples
    return sum_of_3 + sum_of_5 - sum_of_15