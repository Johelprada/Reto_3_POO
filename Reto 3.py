class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total_price(self) -> float:
        return self.price


class Cafe(MenuItem):
    def __init__(self):
        super().__init__("Café", 2.0)


class Postre(MenuItem):
    def __init__(self):
        super().__init__("Pastel de Chocolate", 4.5)


class Agua(MenuItem):
    def __init__(self):
        super().__init__("Agua", 1.0)


class CocaCola(MenuItem):
    def __init__(self):
        super().__init__("Coca Cola", 1.5)


class Nachos(MenuItem):
    def __init__(self):
        super().__init__("Nachos", 3.5)


class Ensalada(MenuItem):
    def __init__(self):
        super().__init__("Ensalada César", 4.0)


class Hamburguesa(MenuItem):
    def __init__(self):
        super().__init__("Hamburguesa", 7.5)


class Pizza(MenuItem):
    def __init__(self):
        super().__init__("Pizza", 9.0)


class TacosVegetarianos(MenuItem):
    def __init__(self):
        super().__init__("Tacos Vegetarianos", 6.5)


class Lasaña(MenuItem):
    def __init__(self):
        super().__init__("Lasaña", 8.0)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.calculate_total_price() for item in self.items)

    def apply_discount(self) -> float:
        total = self.calculate_total()
        if len(self.items) >= 5:
            return total * 0.9
        return total

    def show_order_summary(self):
        print("🧾 Resumen del pedido:")
        for item in self.items:
            print(f"- {item.name} (${item.price:.2f})")
        print(f"Total: ${self.calculate_total():.2f}")
        print(f"Total con descuento (si aplica): ${self.apply_discount():.2f}")


def main():

    orden = Order()

    orden.add_item(Cafe())
    orden.add_item(Postre())
    orden.add_item(Hamburguesa())
    orden.add_item(Pizza())
    orden.add_item(Ensalada())


    orden.show_order_summary()


if __name__ == "__main__":
    main()
