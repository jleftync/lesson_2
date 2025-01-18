
import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

#The user accesses initial and language key
def get_data(key, language):
    return data.get(key, {}).get(language, key)

# Now 'data' contains the contents
# of the JSON file as a Python dictionary or list
def prompt(message):
    print(f"==> {message}")

#to make sure numbers calculate correctly
#require user to enter a float
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False
##Asks user which language to choose
##By going to JSON file.  Brackets good
## or one entry but not more
prompt(data['LanguageEntry'])
language = input()
##ensures selected language will be
##english or spanish by requiring en or es
while language not in ["en", "es"]:
    prompt(data['UnknownLanguage'])
    language = input()

## we could also have done this data[][] if 
## we had the language key set to variable
prompt(get_data('Welcome', language))

##to ensure continuous operation everything
##is nested in a while loop
while True:
    prompt(get_data('FirstNumber', language))
    number1 = input()

    while invalid_number(number1):
        prompt(get_data('WrongNumber', language))
        number1 = input()

    prompt(get_data('SecondNumber', language))
    number2 = input()

    while invalid_number(number2):
        prompt(get_data('WrongNumber', language))
        number2 = input()

    prompt(get_data('OperationSelect', language))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(get_data('CorrectOperation', language))
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(get_data('Result', language).format(output=output))
    prompt(get_data('MoreCalculation', language))
    answer = input()

    while answer not in ["1", "2"]:
        prompt(get_data('ChooseYesOrNo', language))
        answer = input()

    match answer:
        case "1":
            continue
        case "2":
            break