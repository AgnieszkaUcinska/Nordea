def second_best(n, arr):
    n = len(arr)
    arr_sorted = sorted(arr, reverse=True)
    set_arr_sorted = set(arr_sorted)
    list_unsorted = list(set_arr_sorted)
    list_sorted = sorted(list_unsorted, reverse = True)
    second_best = list_sorted[1]
    return second_best
    print (second_best)