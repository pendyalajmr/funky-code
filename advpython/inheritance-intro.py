#Inheritance

class Decimal:

    def __init__(self, number, precision):
        self.number = number
        self.precision = precision

    def __repr__(self):
        return "%.2f" % self.number

print(Decimal(48.5858588585858, 2))