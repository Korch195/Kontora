from itertools import combinations_with_replacement

def partitions(n):
    # Generate all partitions of n
    if n == 0:
        yield []
        return
    for p in partitions(n - 1):
        yield [1] + p
        if p and p[0] < n:
            yield [p[0] + 1] + p[1:]

def part(n):
    products = set()
    for partition in partitions(n):
        product = 1
        for num in partition:
            product *= num
        products.add(product)
    
    sorted_products = sorted(products)
    length = len(sorted_products)
    range_val = sorted_products[-1] - sorted_products[0]
    average = sum(sorted_products) / length
    
    if length % 2 == 0:
        median = (sorted_products[length // 2 - 1] + sorted_products[length // 2]) / 2
    else:
        median = sorted_products[length // 2]
    
    return f"Range: {range_val} Average: {average:.2f} Median: {median:.2f}"
