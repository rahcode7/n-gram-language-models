import sys
import timeit


list_size = 5000
range_size = int(sys.argv[1])


from collections import defaultdict, Counter
import random
random.seed('MY SEED!')
range_size = """ + str(range_size) + """
list_size = """ + str(list_size) + """
initial_list = [random.randint(0, range_size) for i in range(list_size)]
def count_if_else(my_list):
    counts = {}
    for item in my_list:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts
def count_if(my_list):
    counts = {}
    for item in my_list:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return counts
def count_exception(my_list):
    counts = {}
    for item in my_list:
        try:
            counts[item] += 1
        except KeyError:
            counts[item] = 1
    return counts
def count_setdefault(my_list):
    counts = {}
    for item in my_list:
        counts.setdefault(item, 0)
        counts[item] += 1
    return counts
def count_fromkeys(my_list):
    counts = dict.fromkeys(my_list, 0)
    for item in my_list:
        counts[item] += 1
    return counts
def count_set_and_comprehension(my_list):
    return dict((item, my_list.count(item)) for item in set(my_list))
def count_defaultdict(my_list):
    counts = defaultdict(int)
    for item in my_list:
        counts[item] += 1
    return counts
def count_counter(my_list):
    return Counter(my_list)
"""


def time_function(func_name):
    timed_code = 'new_list = initial_list[:]; {}(new_list)'.format(func_name)
    time = min(timeit.Timer(timed_code, setup=setup).repeat(7, 1000))
    print("{} with time: {}".format(func_name, time))


print("List of {} random numbers generated in range 0 to {}"
      .format(list_size, range_size))
time_function("count_if_else")
time_function("count_if")
time_function("count_exception")
time_function("count_setdefault")
time_function("count_fromkeys")
time_function("count_defaultdict")
time_function("count_counter")