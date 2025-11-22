def time_to_run(f):
    """
    this function will give n in the wrapper function that is length of list
    and it will store start time and end time of function f(n) to know how long
    does it take to finish it
    """
    def wrapper(n):
        import time
        start = time.perf_counter()
        f(n)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"{elapsed_time:.6f}")
    return wrapper

@time_to_run
def make_a_list(n):
    """
    this function makes a list from 1 to n
    """
    my_list = []
    for i in range(1, n+1):
        my_list.append(i)
    return my_list

make_a_list(2000000)
