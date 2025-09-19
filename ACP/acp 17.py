total_amount=4
amount_paid=2.5
def calc_return():
    a=total_amount-amount_paid
    return a

returned_amount=calc_return()
print("Vishal has to return to shopkeeper:",returned_amount,'$')