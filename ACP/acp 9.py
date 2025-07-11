print("choose your transport below")
transport_options_1=input("enter 1 for bike and 2 for car: ")

if transport_options_1=="1":
    print("you have chosen bike")
    transport_options_3=input("pulsar or KTM:")
    if transport_options_3=="pulsar":
       print("you have chosen pulsar")
       print("your travelling cost is 5000rs.")
    elif transport_options_3=="KTM":
       print("you have chosen KTM")
       print("your travelling cost is 7000rs.")
elif transport_options_1=="2":
    print("you have chosen car")
    transport_option_4=input("Rolls royce or KIA:")
    if transport_option_4=="Rolls royce":
       print("you have chosen rolls royce:")
       print("your travelling cost is 150,000rs.")
    elif transport_option_4=="KIA":
       print("you have chosen KIA")
       print("your travelling cost is 700,000rs.")
else:
    print("you have not chosen any transport \n your transport is not valid")