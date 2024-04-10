from statistics import mean, median

def part(n):
    partitions = [{1}]
    for k in range(1, n+1):
        new_set = set()
        for x in range(1, k+1):
            for y in partitions[k - x]:
                new_set.add(x * y)
        partitions.append(new_set)
    pprod = partitions[n]
    return 'Range: {} Average: {:.2f} Median: {:.2f}'.format(max(pprod) - min(pprod), mean(pprod), median(pprod))