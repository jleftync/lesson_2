
import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)


# Now 'data' contains the contents of the JSON file as a Python dictionary or list
def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(data['Welcome'])

while True:
    prompt(data['FirstNumber'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['WrongNumber'])
        number1 = input()

    prompt(data['SecondNumber'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['WrongNumber'])
        number2 = input()

    prompt(data['OperationSelect'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data['CorrectOperation'])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(data['Result'].format(output=output))
    prompt(data['MoreCalculation'])
    answer = input()

    while answer not in ["1", "2"]:
        prompt(data['ChooseYesOrNo'])
        answer = input()
    
    match answer:
        case "1":
            continue
        case "2":
            break