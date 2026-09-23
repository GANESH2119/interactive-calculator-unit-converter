# 🧮 Interactive Calculator & Unit Converter

## 1. About the Project

Interactive Calculator & Unit Converter is a Python-based command-line application designed to perform basic arithmetic calculations and common unit conversions through a simple and user-friendly terminal interface.

The project combines a basic calculator with useful conversion utilities. Users can perform arithmetic operations such as addition, subtraction, multiplication, and division, as well as convert distances from kilometers to miles and temperatures from Celsius to Fahrenheit.

The application focuses on fundamental Python programming concepts such as functions, conditional statements, loops, user input handling, mathematical operations, input validation, and error handling.

The project was developed as part of an internship task to demonstrate practical understanding of Python syntax, control flow, functions, and interactive command-line programming.

---

## 2. Features

- ➕ Addition of two numbers
- ➖ Subtraction of two numbers
- ✖️ Multiplication of two numbers
- ➗ Division of two numbers
- 📏 Kilometer to Miles conversion
- 🌡️ Celsius to Fahrenheit conversion
- 🔄 Interactive menu-driven interface
- 🔢 User input handling
- 🛡️ Input validation
- ⚠️ Error handling for invalid inputs
- 🚫 Division-by-zero protection
- 🔁 Continuous execution using loops
- ❌ Easy exit option
- 💻 Simple terminal-based interface
- 📊 Accurate mathematical calculations

---

## 3. Technologies Used

- Python 3
- Python Functions
- Conditional Statements
- While Loops
- User Input
- Arithmetic Operators
- Mathematical Formulas
- Exception Handling
- Input Validation
- Command-Line Interface (CLI)

---

## 4. Project Overview

The application provides a menu-driven interface where users can select different operations.

The main menu contains the following options:

    =========================================
       INTERACTIVE CALCULATOR & UNIT CONVERTER
    =========================================

    1. Basic Calculator
    2. Kilometers to Miles
    3. Celsius to Fahrenheit
    4. Exit

    Enter your choice:

### ➕ Basic Calculator

The Basic Calculator allows users to perform four fundamental arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division

The user enters two numbers and selects the required operation.

Example:

    Enter first number: 25
    Enter second number: 5

    Select operation:
    + Addition
    - Subtraction
    * Multiplication
    / Division

    Enter operation: *

    Result: 125

The calculator processes the input using arithmetic operators and displays the calculated result.

---

### 📏 Kilometer to Miles Conversion

The application provides a simple distance conversion from kilometers to miles.

The conversion is performed using the standard formula:

    Miles = Kilometers × 0.621371

Example:

    Enter distance in kilometers: 10

    Distance in miles: 6.21371

This feature demonstrates the use of mathematical formulas and numerical input processing in Python.

---

### 🌡️ Celsius to Fahrenheit Conversion

The application also converts temperature from Celsius to Fahrenheit.

The standard conversion formula used is:

    Fahrenheit = (Celsius × 9/5) + 32

Example:

    Enter temperature in Celsius: 25

    Temperature in Fahrenheit: 77.0

This demonstrates how mathematical formulas can be implemented in a Python program to perform real-world unit conversions.

---

### 🔄 Menu-Driven Program

The complete application operates through a continuous menu-driven system.

A loop keeps the program running so that the user can perform multiple operations without restarting the application.

The user can return to the main menu after completing an operation and select another feature.

The program terminates only when the user selects the Exit option.

---

### 🛡️ Input Validation

Input validation is implemented to handle incorrect or unexpected user input.

The program checks user entries before performing calculations and conversions.

This helps prevent the application from crashing when the user enters invalid values.

Examples of handled situations include:

- Invalid menu choices
- Non-numeric input
- Invalid calculator operations
- Division by zero
- Incorrect user input

---

### ⚠️ Error Handling

The application includes error-handling mechanisms to provide a smoother user experience.

For example, division by zero is prevented and the user receives an appropriate message instead of the program terminating unexpectedly.

Similarly, invalid inputs are handled using validation and exception-handling techniques.

---

### 🔁 Continuous User Interaction

The application uses a loop-based structure to continuously accept user commands.

The general workflow is:

    Start Application
          ↓
    Display Main Menu
          ↓
    Get User Choice
          ↓
    ┌───────────────┐
    │ Select Option │
    └───────────────┘
          ↓
    ┌────────┬──────────────┬──────────────┐
    │        │              │              │
 Calculator  KM → Miles   °C → °F        Exit
    │        │              │              │
    └────────┴──────────────┴──────────────┘
          ↓
    Display Result
          ↓
    Return to Main Menu
          ↓
       Continue
          ↓
         Exit

This structure makes the application interactive and easy to use.

---

## 5. How to Run

### Step 1: Clone the Repository

    git clone https://github.com/GANESH2119/interactive-calculator-unit-converter.git

### Step 2: Open the Project Folder

    cd interactive-calculator-unit-converter

### Step 3: Run the Python Program

    python calculator_converter.py

### Step 4: Use the Application

After running the program, the main menu will appear in the terminal.

Select the required option and enter the requested values.

Example:

    1. Basic Calculator
    2. Kilometers to Miles
    3. Celsius to Fahrenheit
    4. Exit

    Enter your choice:

The application will display the result and allow the user to perform another operation.

---

## 👨‍💻 Developer

**Ganesh Pudi**
