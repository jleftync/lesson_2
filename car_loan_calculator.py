
import json

# Open the JSON file for reading
with open('car_loan_monthly_calculator.json', 'r') as file:
    data = json.load(file)

#The user accesses initial and language key
##def get_data(key, language):
##    return data.get(key, {})

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

def not_in_dollars_and_cents(loan_value_str):

    try:
        value = str(loan_value_str)
        if len(value.rsplit('.', maxsplit=1)[-1]) > 2:
            raise ValueError
    except ValueError:
        return True

    return False

##Asks user which language to choose
##By going to JSON file.  Brackets good
## or one entry but not more


## we could also have done this data[][] if
## we had the language key set to variable
prompt(data['Welcome'])

##to ensure continuous operation everything
##is nested in a while loop
while True:
    prompt(data['LoanAmount'])
    total_loan_amount = input()

    while invalid_number(total_loan_amount):
        prompt(data['NotNumericalValue'])
        total_loan_amount = input()

    while not_in_dollars_and_cents(total_loan_amount):
        prompt(data['WrongValue'])
        total_loan_amount = input()

    prompt(data["LoanDuration"])
    loan_duration_years = input()

    while invalid_number(loan_duration_years):
        prompt(data['WrongDuration'])
        loan_duration_years = input()

    prompt(data['APRSelect'])
    apr = float(input()) * 0.01

    while invalid_number(total_loan_amount):
        prompt(data['WrongApr'])
        total_loan_amount = float(input()) * 0.01

    while invalid_number(apr):
        prompt(data['WrongValue'])
        apr = input() *0.01



    monthly_interest = float(apr) / 12
    ##print(monthly_interest)
    loan_duration_in_months = float(loan_duration_years) * 12
    ##print(loan_duration_in_months)
    monthly_payment = float(total_loan_amount) * \
        (monthly_interest / (1 - (1 + monthly_interest) ** \
                             (-loan_duration_in_months)))
    prompt(data['Result'].format(monthly_payment=monthly_payment))
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