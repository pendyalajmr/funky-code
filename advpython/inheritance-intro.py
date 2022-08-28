#Inheritance
class Decimal:

    def __init__(self,  number, precision):
        self.number = number
        self.precision = precision

    def __repr__(self):
        return "%.{}f".format(self.precision) % self.number

class Currency(Decimal):
    def __init__(self, symbol, number, precision):
        super().__init__(number, precision)
        self.symbol = symbol

    def __repr__(self):
        return "{}{}".format(self.symbol, super().__repr__())


print(Decimal(48.5858588585858, 2))
print(Currency('Rs.', 49.5858588585858, 1))
