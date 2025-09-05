def shutdown():
    check_1=input("has the user closed all tabs:")
    check_2=input("has the user saved all the content:")
    check_3=input("can the system start shutting down:")

    if check_1=="yes" and check_2=="yes" and check_3=="yes":
        print("shutting down")
    elif check_1=="no" or check_2=="no" or check_3== "no":
        print("sorry")
    else:
        print("sorry")


shutdown()