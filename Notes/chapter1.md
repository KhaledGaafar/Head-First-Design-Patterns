# Chapter 1: Welcome to Design Patterns

## Introduction to Design Patterns
The best way to use patterns is to load your brain with them and then recognize places in your designs and existing applications where you can apply them.

---

## Core Observations

* **Inheritance Limitations:** Inheritance might be good for code reuse, but it is not always a good solution—especially when considering long-term maintenance.
* **The Reality of Software:** Software change is a constant rule. Always be careful about parts that are subject to change versus parts that remain stable.
* **OO Basics vs. OO Design:** Knowing abstraction, encapsulation, inheritance, and polymorphism does not automatically make you a good OO designer. Design principles and patterns address how systems cope with change.

---

## Key Design Principles

> **Design Principle 1:**  
> Identify the aspects of your application that vary and separate them from what stays the same.

> **Design Principle 2:**  
> Program to an interface, not an implementation.  
> *(Interface means a supertype—an abstract class or interface—so polymorphism can handle dynamic runtime objects.)*

> **Design Principle 3:**  
> Favor composition over inheritance.  
> *(Putting two classes together via HAS-A relationships offers far more flexibility than IS-A relationships.)*

---

## Strategy Pattern: Encapsulating Behaviors

### 1. Behavior Classes vs. Subclass Implementation
* **The Problem:** Implementing behaviors directly inside subclass implementations or relying purely on inheritance causes code duplication and rigid structures.
* **The Solution:** Extract varying behaviors (such as `FlyBehavior` and `QuackBehavior`) into dedicated classes that implement a specific behavior interface.
* **Delegation:** The main class (`Duck`) delegates behavior execution to these behavior objects rather than writing the logic directly.

### 2. "Program to an Interface" Explained
* Always declare variables using their supertype (`Animal animal = new Dog();`) rather than concrete classes (`Dog d = new Dog();`). This prevents locking your code into specific concrete implementations.

### 3. Dynamic Behavior Assignment (Runtime Switching)
By including setter methods in the parent class, behaviors can be swapped dynamically while the program is running:

---

## Official Pattern Definition

> **The Strategy Pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

* **Family of Algorithms:** The encapsulated behavior implementations (e.g., `FlyWithWings`, `FlyNoWay`, `FlyRocketPowered`).
* **Interchangeable:** Any class implementing the behavior interface can be plugged into the client at compile time or runtime.

---

## The Power of a Shared Vocabulary

Communicating using pattern names (e.g., saying *"We are using the Strategy Pattern"* instead of detailing every class setup):

1. **Says more with less:** Immediately conveys structure, relationships, and trade-offs.
2. **Keeps discussion at the design level:** Prevents discussions from prematurely degrading into low-level code details.
3. **Elevates team efficiency:** Reduces misunderstandings and helps team members learn OO best practices faster.