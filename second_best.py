def second_best (n, arr)
    arr = []
    arr_sorted = sorted(arr, reverse=True)
    first_score = max(arr_sorted)
    set_arr_sorted = set(arr_sorted)
    modified_set_arr_sorted = set_cdslckldkcarr_sorted - first_score
    second_best = max(modified_set_arr_sorted)
    print (second_best)