# skończone

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)


def orientation(p1: Point, p2: Point, p3: Point):
    val = (p2.y - p1.y)*(p3.x - p2.x) - (p3.y - p2.y)*(p2.x - p1.x)
    if val > 0:
        return 1    # prawoskretne
    elif val < 0:
        return -1   # lewoskretne
    else:
        return 0    # wspolliniowe


def jarvis1(points):
    start_point = points[0]
    for index, point in enumerate(points):
        if point.x < start_point.x:
            start_point = point
        elif point.x == start_point.x:
            if point.y < start_point.y:
                start_point = point

    def next_idx(index):
        if index == len(points) - 1:
            return 0
        return index + 1

    p = start_point
    next_p = None
    result = []

    while next_p != start_point:
        result.append(p)
        idx = next_idx(points.index(p))
        q = points[idx]
        for r in points:
            if r != p and r != q:
                if orientation(p, q, r) == 1:
                    q = r
        p = q
        next_p = p

    return result


def jarvis2(points):
    start_point = points[0]
    for index, point in enumerate(points):
        if point.x < start_point.x:
            start_point = point
        elif point.x == start_point.x:
            if point.y < start_point.y:
                start_point = point

    def next_idx(index):
        if index == len(points) - 1:
            return 0
        return index + 1

    p = start_point
    next_p = None
    result = []

    while next_p != start_point:
        result.append(p)
        idx = next_idx(points.index(p))
        q = points[idx]
        for r in points:
            if r != p and r != q:
                if orientation(p, q, r) == 1:
                    q = r
                elif orientation(p, q, r) == 0:
                    if (p.x <= q.x <= r.x or p.x >= q.x >= r.x) and (p.y <= q.y <= r.y or p.y >= q.y >= r.y):
                        q = r
        p = q
        next_p = p

    return result


polygon1 = []
for i in [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]:
    polygon1.append(Point(i[0], i[1]))

polygon2 = []
for i in [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]:
    polygon2.append(Point(i[0], i[1]))

polygon3 = []
for i in [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]:
    polygon3.append(Point(i[0], i[1]))

print(jarvis1(polygon3))
print(jarvis2(polygon3))
