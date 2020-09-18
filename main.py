import time
import psutil
import os

"""
1. Написать декоратор, замеряющий время выполнение декорируемой функции.
"""


def show_time(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        print('time taken:', time.time() - start_time)
    return wrapper


"""
2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
(создание объектов оформить в виде функций).
"""
num = 1000000

@show_time
def number_list_append(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    print('List has been appended')
    return numbers


@show_time
def number_list_gen(n):
    num_list = [i for i in range(1, n+1)]
    print('List has been generated')
    return num_list


@show_time
def number_generator(n):
    print('Generator created')
    for i in range(1, n+1):
        yield print(i)


number_list_append(num)
print()
number_list_gen(num)
print()

print('Generator created')
number_generator(num)
print()
print()

"""
3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
"""


def memory_measurement(f):
    def wrapper(*args, **kwargs):
        mem_used_before = psutil.Process(os.getpid()).memory_info().rss/1000000
        print('Memory used before function execution: ' + str(mem_used_before))
        f(*args, **kwargs)
        mem_used_after = psutil.Process(os.getpid()).memory_info().rss/1000000
        print('Memory used after function execution: ' + str(mem_used_after))
        mem_difference = mem_used_after - mem_used_before
        print('Memory used for function execution: ' + str(mem_difference))
    return wrapper


"""
4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: 
натуральные числа от 1 до 1000000.
"""


@memory_measurement
def number_list_append(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    print('List has been appended')
    return numbers


@memory_measurement
def number_list_gen(n):
    num_list = [i for i in range(1, n+1)]
    print('List has been generated')
    return num_list


@memory_measurement
def number_generator(n):
    print('Generator created')
    for i in range(1, n+1):
        yield print(i)




number_list_append(num)
print()
number_list_gen(num)
print()

print('Generator created')
number_generator(num)
