balance = 10000
while True:
    tran = input("Enter tran type deb/cre or 'stop' to exit: ")
    if tran == "stop":
        break
    elif tran == "deb":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Remaining balance: {balance}")
        else:
            print("Insufficient balance")
    elif tran == "cre":
        amount = int(input("Enter amount: "))
        balance += amount
        print(f"Remaining balance: {balance}")
    else:
        print("Invalid transaction type")
