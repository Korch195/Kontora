def _part(n):
    if type(n) is int:
        n = list(range(1, n + 1))

    stack = [(n, [])]
    parts = [[] for _ in range(max(n) + 1)]
    parts[0] = [[]]

    while stack:
        current_n, current_parts = stack.pop()

        for i in range(1, len(current_n) + 1):
            for j in range(current_n[i - 1]):
                new_parts = current_parts.copy()
                new_parts.append([current_n[i - 1] - j] + [x for x in current_parts[-1] if x != current_n[i - 1] - j])
                stack.append((current_n[:i - j], new_parts))

    return parts[-1]
def part(n):
    def _part(n):
        if type(n) is int:
            n = list(range(1, n + 1))

        stack = [(n, [])]
        parts = [[] for _ in range(max(n) + 1)]
        parts[0] = [[]]

        while stack:
            current_n, current_parts = stack.pop()

            for i in range(1, len(current_n) + 1):
                for j in range(current_n[i - 1]):
                    new_parts = current_parts.copy()
                    new_parts.append([current_n[i - 1] - j] + [x for x in current_parts[-1] if x != current_n[i - 1] - j])
                    stack.append((current_n[:i - j], new_parts))

        return parts[-1]

    sub_arrays = _part(n)
    products = [math.prod(sub_array) for sub_array in sub_arrays]
    min_product = min(products)
    max_product = max(products)
    total_product = sum(products)
    average_product = total_product / len(products)

    products.sort()
    median_product = products[len(products) // 2] if len(products) % 2 else (products[(len(products) - 1) // 2] + products[len(products) // 2]) / 2

    return f"Range: {max_product - min_product} Average: {round(average_product, 2)} Median: {round(median_product, 2)}"