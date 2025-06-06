class CoffeeMaker:
    def __init__(self):
        self.resource = {
            "water":300,
            "milk":200,
            "coffee":100,
        }

    def report(self):
        """Print a report of all resources."""
        print(f"Water:{self.resource['water']}ml")
        print(f"Milk:{self.resource['milk']}ml")
        print(f"Coffee:{self.resource['coffee']}ml")

    def is_resource_sufficient(self, drink):
        """Return True When order can be made, False if ingredients are in insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resource[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resource[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")