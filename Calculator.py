while True:
    print("\n============== PYTHON CALCULATOR =============")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = input("\n Enter your choice from (1-5): ")


    if choice == "5" :
        print("Thanks for using the Calculator . Goodbye!")
        break


    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))


    if choice == "1":
        print("Result :",num1 + num2 )
        
    elif choice =="2":
          print("Result :" , num1 - num2)
     
    elif choice == "3":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif choice == "4":
        print("Result:", num1 * num2)     