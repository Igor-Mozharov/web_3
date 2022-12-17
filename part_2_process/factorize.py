from time import  time
from multiprocessing import  Process, cpu_count, RLock, Pool

lock = RLock()


def factorize(list_numbers, locking = lock ):
    new_list = []
    for number in list_numbers:
        new_list.append([x for x in range(1, number + 1) if number % x == 0])
    return new_list


if __name__ == '__main__':
    print(f'Hey!, there is {cpu_count()} cores on your machine!')
    start_time = time()
    print(factorize([10, 33, 1100, 24567, 24598600]))
    print(f'Simple operation time = {time() - start_time}')
    fin_time = time()
    with Pool(processes=cpu_count()) as pool:
        pool.map_async(factorize, ([10, 33, 1100, 24567, 24598600], ))
    print(f'Multiprocessing operation time = {time() - fin_time}')

