from multiprocessing import Pool


def square_up(number):
    return number ** 2


if __name__ == '__main__':
    # pool = Pool(processes=2)
    # print(pool.map(square_up, range(10)))

    pool = Pool(processes=2)
    result = pool.map_async(square_up, range(10))
    print(result.get(timeout=1))