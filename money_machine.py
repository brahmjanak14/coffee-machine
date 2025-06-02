class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUE = {
        "quarters":0.25,
        "dimes":0.10,
        "nickles":0.05,
        "pennies":0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print the current profit"""
        print(f"Money:{self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Return the total calculated from coins inserted """
        print("Please Insert Coins.")
        for coin in self.COIN_VALUE:
            self.money_received += int(input(f"How Many {coin}?:")) * self.COIN_VALUE[coin]
        return self.money_received

    def make_payment(self, cost):
        """Return True When payment is accepted , or false if insufficient"""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. \nMoney refunded")
            self.money_received = 0
            return False