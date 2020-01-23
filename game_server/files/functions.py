from math import sqrt


def diff_to_min(a, b, c):
    if c in range(a, b):
        return 0
    return min(abs(c - a), abs(c - b))


def object_to_point_diff(obj, point_pos):
    dx = diff_to_min(obj.x, obj.x + obj.szx, point_pos[0])
    dy = diff_to_min(obj.y, obj.x + obj.szy, point_pos[1])
    return min(dx, dy)


# Функция расстояния между двумя точками
def diff(*args):
    if len(args) == 2:
        return diff(*args[0], *args[1])
    x1, y1, x2, y2 = args
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def sign(p):
    if p == 0:
        return 1
    return p // abs(p)


if __name__ == '__main__':
    print(diff((0, 1), (3, 5)))