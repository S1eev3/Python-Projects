from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
# This function is stating to pass an argument but we won't tell how
# or what type of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
# Defining how to implement the payment function from its parent paySlip class
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $200 limit ".format(amount))


obj = DebitCardPayment()
obj.paySlip("$300")
obj.payment("$300")
