# Chapter 1: Welcome to Design Patterns

## Introduction to Design Patterns

The best way to use patterns is to load your brain with them and then recognize places in your designs and existing applications where you can apply them.

---

## Core Observations

* **Inheritance Limitations:** Inheritance might be good for code reuse, but it is not always a good solution—especially when considering long-term maintenance.
* **The Reality of Software:** Software change is a constant rule. Always be careful about parts that are subject to change versus parts that remain stable.

---

## Key Design Principles

> **Design Principle 1:**  
> Identify the aspects of your application that vary and separate them from what stays the same.

> **Design Principle 2:**  
> Program to an interface, not an implementation.

> **Design Principle 3:**  
> Favor composition over inheritance.

---

### 1. Behavior Classes vs. Subclass Implementation
* **The Problem:** Implementing behaviors directly in subclass implementations or relying purely on inheritance causes code duplication and rigid structures.
* **The Solution:** Extract varying behaviors (such as `FlyBehavior` and `QuackBehavior`) into dedicated classes that implement a specific behavior interface.
* **Delegation:** The main class (`Duck`) delegates behavior execution to these behavior classes rather than writing the implementation logic directly.

### 2. "Program to an Interface" Explained
* **Supertype Concept:** "Interface" refers to a general **supertype** (an abstract class or Java `interface`).
* **Polymorphism in Action:** Always declare variables using their supertype (`Animal animal = new Dog();`) rather than concrete classes (`Dog d = new Dog();`). This prevents locking your code into specific concrete classes.

### 3. Has-A over Is-A (Composition)
* Instead of deriving behavior from inheritance ("Is-A"), classes gain behavior by containing behavior objects ("Has-A").
* Allows behaviors to be assigned or swapped dynamically at runtime using setter methods.