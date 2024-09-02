import random
import timeit

# import matplotlib.pyplot as plt


def test_func(sorting_func, n_array_length, repeat=5, number=1e6):
    """_summary_

    Args:
        sorting_func (_type_): _description_
        n_array_length (_type_): _description_
        repeat (int, optional): _description_. Defaults to 5.
        number (_type_, optional): _description_. Defaults to 1e6.
    """
    
    test_case = [random.randint(0, 10000) for i in range(n_array_length)]
    exec_res = timeit.repeat("sorting_func(test_case)", repeat=repeat, number=number, globals=locals())
    res = min(exec_res) / number * 1000

    return res


def check_sorting(sorting_func, n_array_length=10, min_elem=0, max_elem=100):
    test_arr = [random.randint(min_elem, max_elem+1) for i in range(n_array_length)]
    print(f"Test case:   {test_arr}")
    sorting_func(test_arr)
    print(f"Test result: {test_arr}")
    print(f"Sorted correctly: {test_arr == sorted(test_arr)}")