"""In this file, we define the benchmark stock market model agent classes"""

from stockmarket.stocks import Stock


class Trader:
    """a base class for Traders"""
    def __init__(self, name, money, bid_ask_spread, memory_size, function):
        """Creates a new trader"""
        self.name = name
        self.money = money
        self.stocks = {}
        # bid ask spread is an integer
        self.bid_ask_spread = bid_ask_spread
        self.memory_size = memory_size
        self.function = function

    def valuate_stocks(self, stock):
        return self.function(stock=stock, memory=self.memory_size)

    def transact(self, inflow_item, inflow_amount, outflow_item, outflow_amount):
        """This allows an agent to transact stocks and money"""
        if type(inflow_item) is Stock and (outflow_amount <= self.money):
            self.stocks[repr(inflow_item)] += inflow_amount
            self.money -= outflow_amount
            print (self, "just purchased", inflow_amount, "stocks.")  # for debugging purposes

        elif type(inflow_item) is str and (outflow_amount <= outflow_item.amount):
            self.money += inflow_amount
            self.stocks[repr(outflow_item)] -= outflow_amount
            print(self, "just sold", outflow_amount, "stocks.")

        else: 
            print("No transaction possible")
            return False

        return True

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "trader_" + str(self.name)

    def show(self):
        print("Name:", self.name)
        print("Money:", self.money)
        print("Stocks:", self.stocks)
        print("")
