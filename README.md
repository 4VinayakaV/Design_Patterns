# Design_Patterns

Link to the repository &nbsp;- https://github.com/4VinayakaV/Design_Patterns

# Factory Method Project

## Project Description

This project demonstrates the **Factory Method** design pattern in Python. The **Factory Method** allows for creating objects without specifying the exact class of the object that will be created. In this example, I have used a `CarFactory` to produce different types of cars based on the provided car type, like `Sedan` and `SUV`. This approach abstracts the car creation process, making it easier to extend the project by adding new car types without modifying the factory interface.

## Requirements

1. **Create Car Factory**: The system must have a `CarFactory` that can produce car objects based on a provided car type.
2. **Create Car Types**: The system must include different types of cars (e.g., `Sedan`, `SUV`).
3. **Drive Method**: Each car type must have a `drive` method that returns a unique string indicating the car type being driven.
4. **Main Program Execution**: The program should allow a user to create car instances through the factory and call the `drive` method to output the result.