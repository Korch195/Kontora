# def sum_of_multiples(n):
def solution(n):
    if n <= 0:
        return 0

    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

# Example usage:
# number = 10
# result = sum_of_multiples(number)
# print(result)  # Output will be 23
