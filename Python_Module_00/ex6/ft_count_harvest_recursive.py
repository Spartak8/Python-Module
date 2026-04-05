def helper(i, n):
    if i > n:
        print("Harvest time!")
        return
    print(f"Day {i}")
    helper(i + 1, n)


def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))
    helper(1, n)
