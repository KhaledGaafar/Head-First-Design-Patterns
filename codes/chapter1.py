from abc import ABC,abstractmethod

#----------------------- Interface Behaviour----------------------
class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        ...
#------------------------ Sets of Classes that implement Interface------
class FlyWithWings(IFlyBehavior):
    def fly(self):
        print("I'm flying!!")
class FlyNoWay(IFlyBehavior):
    def fly(self):
        print("I can't fly")


#----------------------- Interface Behaviour----------------------
class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        ...
#------------------------ Sets of Classes that implement Interface------
class Quack(IQuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(IQuackBehavior):
    def quack(self):
        print("<< Silence >>")
class Squeak(IQuackBehavior):
    def quack(self):
        print("Squeak")


#-------------- Base Duck Class ------------
class Duck:

    def __init__(self):
        self.fly_behavior: IFlyBehavior
        self.quack_behavior: IQuackBehavior

    def perform_fly(self):
        self.flyBehavior.fly()

    def perform_quack(self):
        self.quackBehavior.quack()

# -------------- Subclass of Duck -----------
class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()


#--------------- quick test ---------------
mallard = MallardDuck()
mallard.perform_fly()
mallard.perform_quack()


