from math import sqrt


# Функция расстояния между двумя точками
def diff(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def diff_to_min(a, b, c):
    if c in range(a, b):
        return 0
    return min(abs(c - a), abs(c - b))


def object_to_point_diff(obj, point_pos):
    dx = diff_to_min(obj.x, obj.x + obj.szx, point_pos[0])
    dy = diff_to_min(obj.y, obj.x + obj.szy, point_pos[1])
    return sqrt(dx ** 2 + dy ** 2)


if __name__ == '__main__':
    pass
    # print(object_to_point_diff())
