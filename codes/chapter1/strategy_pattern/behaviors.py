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

class FlyRocketPowered(IFlyBehavior):
    def fly(self) :
        print("I'm flying with a rocket!")


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