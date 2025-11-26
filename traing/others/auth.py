balance=10000
debit=int(input("Enter amount to debit: "))

if debit<=balance:
    balance-=debit
    print(f"remaing balance:{balance}")
else:
    print("dont have balance!")
