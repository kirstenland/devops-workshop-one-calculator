def calculate_sum(operation, first_number, second_number):
    if operation == "+":
        return first_number + second_number
    elif operation == "x":
        return first_number * second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "/":
        return first_number / second_number
    elif operation == "%":
        return first_number % second_number
    elif operation == "^":
        return first_number ** second_number
