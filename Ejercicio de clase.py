import math

# Clase Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Clase Line
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
        self.points = []  # Para discretize_line

    def compute_length(self):
        return math.sqrt((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)

    def compute_slope(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        if dx == 0:
            return float('inf')  # línea vertical
        return math.degrees(math.atan2(dy, dx))

    def compute_horizontal_cross(self):
        return (self.start.y <= 0 <= self.end.y) or (self.end.y <= 0 <= self.start.y)

    def compute_vertical_cross(self):
        return (self.start.x <= 0 <= self.end.x) or (self.end.x <= 0 <= self.start.x)

    def discretize_line(self, n):
        self.points = []
        for i in range(n + 1):
            t = i / n
            x = self.start.x + t * (self.end.x - self.start.x)
            y = self.start.y + t * (self.end.y - self.start.y)
            self.points.append(Point(x, y))

# Clase Rectangle usando composición de 4 líneas
class Rectangle:
    def __init__(self, l1, l2, l3, l4):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4

# -------------------
# Ejemplo de uso real:
# -------------------

if __name__ == "__main__":
    # Crear puntos
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)

    # Crear líneas del rectángulo
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)

    # Crear rectángulo
    rect = Rectangle(l1, l2, l3, l4)

    # Mostrar propiedades de una línea
    print("Línea l1:")
    print("  Longitud:", l1.length)
    print("  Pendiente (°):", l1.slope)
    print("  Cruza eje X:", l1.compute_horizontal_cross())
    print("  Cruza eje Y:", l1.compute_vertical_cross())

    # Discretizar línea
    print("\nPuntos discretizados en l1:")
    l1.discretize_line(5)
    for pt in l1.points:
        print(f"  ({pt.x:.2f}, {pt.y:.2f})")
