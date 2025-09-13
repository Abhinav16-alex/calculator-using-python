# calculator-using-python
A simple yet robust command-line calculator built in Python for basic arithmetic operations.

##  Project Overview

This calculator application was developed as part of the Python Developer Internship task. It provides a user-friendly command-line interface for performing basic mathematical operations with proper error handling and input validation.

##  Features

- **Four Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Error Handling**: Handles division by zero, invalid inputs, and unexpected errors
- **User-Friendly Interface**: Clear prompts and formatted output
- **Continuous Operation**: Loop until user chooses to exit
- **Input Validation**: Ensures only valid numbers are processed
- **Professional Structure**: Well-organized code with proper functions

##  How to Run

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd calculator-cli-app
   ```

2. **Run the calculator**:
   ```bash
   python calculator.py
   ```
   or
   ```bash
   python3 calculator.py
   ```

##  Usage Example

```
==================================================
     WELCOME TO CALCULATOR CLI APP
==================================================
Supported operations: Addition, Subtraction, Multiplication, Division
Type 'quit' or 'exit' when prompted to close the calculator

------------------------------

Select operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
Enter choice (1/2/3/4): 1
Enter first number: 15
Enter second number: 25

15.0 + 25.0 = 40.0

Do you want to perform another calculation?
Enter 'yes' to continue or any other key to exit: no

Thank you for using Calculator CLI App!
Goodbye! 
```

##  Technical Implementation

### Key Concepts Used:
- **Functions**: Separate function for each operation (`add`, `subtract`, `multiply`, `divide`)
- **Loops**: Continuous operation until user exits
- **Conditionals**: Input validation and operation selection
- **CLI Interaction**: User input handling with `input()` function
- **Error Handling**: Try-except blocks for robust error management

### Code Structure:
```
calculator.py
├── Operation functions (add, subtract, multiply, divide)
├── Input handling functions (get_number, get_operation)
├── Display functions (display_result, display_welcome)
└── Main function with program loop
```

##  Requirements

- Python 3.x
- No external libraries required (uses only built-in Python functions)

##  Features Demonstrated

1. **Function-based Architecture**: Each operation is implemented as a separate function
2. **User Input Handling**: Robust input collection using `input()` with validation
3. **Loop Control**: Continuous operation with proper exit conditions
4. **Error Management**: Comprehensive error handling for edge cases
5. **Clean Code Practices**: Well-commented, readable code structure

##  Learning Outcomes

Through this project, I gained experience in:
- Structuring Python applications with functions
- Implementing user input validation
- Handling exceptions and edge cases
- Creating intuitive command-line interfaces
- Writing clean, maintainable code

##  Task Completion

 Functions for each operation (+, -, *, /)  
 User input using input()  
 Loop until user chooses to exit  
 Well-structured code schema  
 Error handling and input validation  
 Professional CLI interface  

---

**Developed by**: [Your Name]  
**Task**: Python Developer Internship - Task 1  
**Submission Date**: [Current Date]
