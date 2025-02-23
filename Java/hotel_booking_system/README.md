# Hotel Booking and Locker Storage System

## Overview

This project consists of two main components:

1. Hotel Booking System: A system to manage different types of hotel rooms (Single, Double, Family), allowing users to book rooms, check availability, and manage occupancy.
2. Locker Storage System: A system to manage package lockers, storing and retrieving mail items for recipients, ensuring appropriate size and availability.

The project is implemented in Java, leveraging Object-Oriented Design principles. It includes exception handling, validation of parameters, and methods to ensure smooth system operation.

## Features

- Hotel Booking System:
    Room Types: Single, Double, and Family rooms with different occupancy limits.
    Booking and Availability: Check room availability and book rooms.
    Price Validation: Ensure room prices are non-negative.

- Locker Storage System:
    Mail Item Management: Create mail items with dimensions and a recipient.
    Locker Management: Add or pick up mail items from lockers, ensuring item fits and matches the recipient.

## Technologies Used

- Java: Core programming language used for the implementation.
- Object-Oriented Programming: For modeling hotel rooms, lockers, and mail items using classes and inheritance.

## How to Run

- Clone the repository or download the project files.
- Compile and run the Java classes:
```
javac HotelBookingSystem.java LockerStorageSystem.java
java HotelBookingSystem
java LockerStorageSystem
```
- The system will interact with you based on predefined methods for booking rooms and managing lockers.

## Key Classes

- HotelBookingSystem: Manages hotel room bookings and availability.
- LockerStorageSystem: Manages locker operations and mail item storage.
- Room: Abstract class for common room behaviors, with subclasses for each room type.
- Recipient: Represents a recipient of a mail item in the locker system.
- MailItem: Represents a package with dimensions and recipient information.
- Locker: Stores mail items and manages their retrieval.

## Exception Handling

- IllegalStateException: Used for invalid room bookings or locker operations.
- IllegalArgumentException: Used for invalid constructor parameters.

This project helps practice Java programming and object-oriented design while handling real-world concepts like hotel management and locker systems.