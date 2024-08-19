def apply_all_func(int_list, *functions):

    results = {}

    for func in functions:
        results[func.__name__] = func(int_list)
    return results


def sum_list(lst):
    return sum(lst)


def max_list(lst):
    return max(lst)


def min_list(lst):
    return min(lst)


# Пример работы кода
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))