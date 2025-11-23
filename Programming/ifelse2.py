#Deposit
balance = 1000

amount = int(input("Enter amount :"))

if amount > 0:
    balance += amount
    print("Balance after deposit :",balance)

else:
    print("Invalid amount")
