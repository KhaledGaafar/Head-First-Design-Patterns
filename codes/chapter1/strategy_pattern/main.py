from Ducks import MallardDuck, ModelDuck
from behaviors import FlyRocketPowered,FlyNoWay


def main():
    print("--- Testing MallardDuck ---")
    mallard = MallardDuck()
    mallard.perform_fly()  # Output: I'm flying!!
    mallard.perform_quack()  # Output: Quack

    print("\n--- Testing Dynamic Behavior Swap (ModelDuck) ---")
    model = ModelDuck()

    # Dynamically assign rocket behavior at runtime!
    model.set_fly_behavior(FlyNoWay())
    model.perform_fly()  # Output: I'm flying with a rocket!


if __name__ == "__main__":
    main()


