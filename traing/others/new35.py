balance=10000
while True:
tran=input("Enter tra type deb/cre/stop: ")
if(type=="stop"):
    break
    amount=float(input("Enter amount:"))
amount=int(input("Enter amount: "))
if tran=="deb":
    if amount<=balance:
        balance-=amount
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient balance")
elif tran=="cre":
    balance += amount
    print(f"Remaining balance:{balance}")
else:
    print("Invalid transaction type")
