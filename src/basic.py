from math import factorial


def mean(my_list):
    return sum(my_list) / len(my_list)


def median(my_list):
    my_list.sort()
    if len(my_list) % 2 == 0:
        median = (my_list[len(my_list) // 2 -1] + my_list[len(my_list) // 2]) / 2
    else:
        median = my_list[(len(my_list) - 1) // 2]
    return median


def weighted_mean(my_list, weight_list):
    weighted_mean = sum(map(lambda i, j: i*j, my_list, weight_list)) / sum(weight_list)
    return weighted_mean


def quartiles(my_list):
    my_list.sort()
    length = len(my_list)
    q2 = median(my_list)
    if length % 2 == 0:
        q1 = median(my_list[:length // 2])
        q3 = median(my_list[length // 2:])
    else:
        q1 = median(my_list[:(length - 1) // 2])
        q3 = median(my_list[(length - 1) // 2 + 1:])
    return q1, q2, q3


def standard_deviation(my_list):
    my_mean = mean(my_list)
    numerator = 0
    for x in my_list:
        numerator += pow((x - my_mean), 2)
    stddev = pow((numerator / len(my_list)), 0.5)
    return stddev


def combination(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))


def permutation(n, r):
    return factorial(n) // factorial(n-r)


def main():
    pass


if __name__ == "__main__":
    main()
