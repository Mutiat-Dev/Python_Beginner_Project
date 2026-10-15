import json

def main():
    pass

def load_file():
    try:
        with open("expenses.json", "r") as file:
            exp = json.load(file)
            return exp
    except (FileNotFoundError, json.JSONDecodeError):
        return []
expenses = load_file()

def update_file(expenses):
    with open("expenses.json", "w")as file:
        json.dump(expenses, file, indent=3)
    
def add_expense(expenses):
    while True:
        amount = (input("Expense Amount: ")).strip()
        if amount == "":
            print("Enter valid input")
            continue
        amount = float(amount)
        break
    while True:
        category = input("Expense Category: Housing | Food | Transport | Internet | Miscellaneous" "\n").strip().title()
        if category == "":
            print("Enter valid input")
        break
    while True:
        description = input("Expense Description: ").strip().title()
        if description == "" :
            print("Enter valid input")
            continue
        break

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    update_file(expenses)

def view_expense(expenses):
    if expenses == []:
        print("No expense yet")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}.{expense["category"]:<5} {expense["description"]:<5} {expense["amount"]:<5}")

def calc_expenses(expenses):
    total_spending = 0

    for expense in expenses:
        total_spending = total_spending + expense["amount"]
    return total_spending

def spend_category(expenses):
    category_totals = {}

    for expense in expenses:
        if expense["category"] in category_totals:
            category_totals[expense["category"]] = category_totals[expense["category"]] + expense["amount"]
        else:
            category_totals[expense["category"]] = expense["amount"]

    return category_totals

def delete(expenses):
    view_expense(expenses)
    while True:
        try:
            choice = int(input("Which expense would you like to remove, pick a number: "))
            break
        except ValueError:
            print("Enter a valid input")   
    if 1 <= choice <= len(expenses):
        choice = choice - 1
        del expenses[choice]
        print("Expense deleted!")
    else:
        print("Invalid Input")

    # print(expenses)
    update_file(expenses)

while True:
    print("\n========EXPENSE TRACKER========")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total spending")
    print("4. Calculate spending by category")
    print("5. Delete an expense")
    print("6. Save and Exit")

    choice = input("Choose an option: ")
    if choice == "1":
            try:
                add_expense(expenses)
                print("Expense Added Succesfully!")
            except ValueError:
                print("Enter a valid option")
    elif choice == "2":
        view_expense(expenses)
    elif choice == "3":
        total = calc_expenses(expenses)
        print(f"Total Expense:",total)
    elif choice == "4":
        spent = (spend_category(expenses))
        for category in spent:
            print(f"{category:<5}{spent[category]:>5}")
    elif choice == "5":
        delete(expenses)
    elif choice == "6":
        update_file(expenses)
        break
    else:
        print("Choose a valid option")
if "__name__" == "__main__":
    main()