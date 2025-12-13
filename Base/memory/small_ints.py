
limit_small_ints = [a is b for a, b in enumerate(range(258))]
true_count_in_list = limit_small_ints.count(True)
false_count_in_list = limit_small_ints.count(False)
print(f"Count True: {true_count_in_list} count False: {false_count_in_list}")
