from behaviors import IFlyBehavior,IQuackBehavior,Quack,FlyWithWings

#-------------- Base Duck Class ------------
class Duck:

    def __init__(self):
        self.fly_behavior: IFlyBehavior
        self.quack_behavior: IQuackBehavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: IFlyBehavior) -> None:
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: IQuackBehavior) -> None:
        self.quack_behavior = qb

# -------------- Subclass of Duck -----------
class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = None
