class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water,
            "milk":milk,
            "coffee":coffee,
        }

class Menu:
    """Models the menu with drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte",water=200,milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=200, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Return all the names of the available menu items"""
        option = ""
        for item in self.menu:
            option += f"{item.name}/"
        return option

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name, Return that item if it exists , otherwise return none"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available")