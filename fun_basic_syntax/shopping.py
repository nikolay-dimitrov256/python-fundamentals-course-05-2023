budget = int(input())

total_spent = 0
overdraft = False

while True:
    command = input()

    if command == "End":
        break

    product_price = int(command)
    total_spent += product_price

    if total_spent > budget:
        overdraft = True
        break

if overdraft:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
