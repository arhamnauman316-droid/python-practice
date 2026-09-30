x = float(input("write number 1: "))
y = float(input("write number 2: "))
history = []

while True:
    try:
        operation = input("choose what to do with that number +,-,x,/, history, clear: ")
        if operation == "quit":
            break
        elif operation == "history":
            if not history:
                print("No history yet.")
            else:
                print(history)

        elif operation == "clear":
            history.clear()
            print("history cleared")

        elif operation == "+":
            result = x + y
            print(result)
            history.append(f"{x} + {y} = {result}")

        elif operation == "/":
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = x / y
            print(result)
            history.append(f"{x} / {y} = {result}")

        elif operation == "-":
            result = x - y
            print(result)
            history.append(f"{x} - {y} = {result}")

        elif operation in ("x", "*"):
            result = x * y
            print(result)
            history.append(f"{x} * {y} = {result}")

        else:
            print("invalid operation")

    except ValueError:
        print("Error: invalid number.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
