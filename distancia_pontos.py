import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    @classmethod
    def from_tuples(cls, tuples):
        points = []
        for i in range(len(tuples)):
            x, y = tuples[i]
            point = cls(x, y)
            points.append(point)
        return points


def compareX(a, b):
    p1 = a
    p2 = b
    return (p1.x - p2.x)

def compareY(a, b):
    p1 = a
    p2 = b
    return (p1.y - p2.y)

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))

def bruteForce(P, n):
    min_dist = float("inf")
    min_points = (None, None)
    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
                min_points = (P[i], P[j])
    return min_dist, min_points

def min(x, y):
    return x if x < y else y

def stripClosest(strip, size, d):
    min_dist = d
    min_points = (None, None)
    strip = sorted(strip, key=lambda point: point.y)

    for i in range(size):
        for j in range(i+1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
                min_points = (strip[i], strip[j])
    return min_dist, min_points

def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n//2
    midPoint = P[mid]
    dl, dl_points = closestUtil(P, mid)
    dr, dr_points = closestUtil(P[mid:], n - mid)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])
    strip_dist, strip_points = stripClosest(strip, len(strip), d)
    if strip_dist < d:
        return strip_dist, strip_points
    if dl < dr:
        return dl, dl_points
    return dr, dr_points

def closest(P, n):
    P = sorted(P, key=lambda point: point.x)
    return closestUtil(P, n)

## Exemplo de uso
#pontos = [
#    Point(1, 2, 'A'),
#    Point(5, 9, 'B'),
#    Point(3, 7, 'C'),
#    Point(2, 4, 'D'),
#    Point(6, 3, 'E')
#]
#
#distancia_minima, pontos_minimos = closest(pontos, len(pontos))
#ponto1, ponto2 = pontos_minimos
#print("Distância mínima:", distancia_minima)
#print("Pontos com distância mínima:", ponto1, ponto2)
