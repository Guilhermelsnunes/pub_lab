class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def buy_drink(self, drink):
        self.wallet -= drink.price 
        self.drunkenness += drink.alcohol_level

    
    