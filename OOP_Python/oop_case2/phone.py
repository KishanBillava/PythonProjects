from items import Item

# Inheritance
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # keyworded arguments
        # call to super funcation to have access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"broken phone {broken_phones} is not greater then zero"

        self.broken_phones = broken_phones