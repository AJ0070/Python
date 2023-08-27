import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")

    while True:
        try:
            expression = input("Enter a mathematical expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                print("Exiting the calculator.")
                break
            
            result = eval(expression)
            print("Result:", result)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    scientific_calculator()
