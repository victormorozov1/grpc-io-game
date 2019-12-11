from math import sqrt


def diff(*args):
    if len(args) == 2:
        return diff(*args[0], *args[1])
    x1, y1, x2, y2 = args
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    print(diff((0, 1), (3, 5)))