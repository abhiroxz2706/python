actual_cost=float(input("enter actual cost:"))
selling_cost=float(input("enter selling cost:"))

if selling_cost > actual_cost:
    amount=selling_cost-actual_cost
    print("profit is:",amount)

else:
    print("no profit")