"""
Calculator CLI App
A command-line calculator supporting basic arithmetic operations
Created for Python Developer Internship
"""

def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation with zero division handling"""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed")
    return a / b

def get_number(prompt):
    """Get a valid number from user input with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    """Get a valid operation from user"""
    operations = {
        '1': ('+', add),
        '2': ('-', subtract), 
        '3': ('*', multiply),
        '4': ('/', divide)
    }
    
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice in operations:
            return operations[choice]
        print("Invalid choice! Please select 1, 2, 3, or 4.")

def display_result(num1, operator, num2, result):
    """Display the calculation result in a formatted way"""
    print(f"\n{num1} {operator} {num2} = {result}")

def display_welcome():
    """Display welcome message and instructions"""
    print("=" * 50)
    print("     WELCOME TO CALCULATOR CLI APP")
    print("=" * 50)
    print("Supported operations: Addition, Subtraction, Multiplication, Division")
    print("Type 'quit' or 'exit' when prompted to close the calculator")

def main():
    """Main calculator function with continuous loop"""
    display_welcome()
    
    while True:
        try:
            print("\n" + "-" * 30)
            
            # Get operation choice
            operator_symbol, operation_func = get_operation()
            
            # Get numbers from user
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            # Perform calculation
            result = operation_func(num1, num2)
            
            # Display result
            display_result(num1, operator_symbol, num2, result)
            
            # Ask if user wants to continue
            print("\nDo you want to perform another calculation?")
            continue_choice = input("Enter 'yes' to continue or any other key to exit: ").strip().lower()
            
            if continue_choice not in ['yes', 'y']:
                print("\nThank you for using Calculator CLI App!")
                print("Goodbye!")
                break
                
        except ValueError as e:
            print(f"\n{e}")
            continue_choice = input("\nDo you want to try again? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                break
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user.")
            print("Thank you for using Calculator CLI App!")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()