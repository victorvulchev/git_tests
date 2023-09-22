def shopping(element):
    command = element
    cart = []
    while(True):
        temp_el = command
        command = input("What would you like to do - add, remove, show, quit:")
        if command == "add":
            cart.append(temp_el)
        elif command == "remove":
            cart.pop
        elif command == "show":
            print(cart)
            command = input("Do you want to add your new item to the cart?")
            if command == "yes":
                cart.append(temp_el)
        else:
            command = input("Add last item to cart before you leave?")
            if command == "yes":
                cart.append(temp_el)
            break
        command = input("Enter a new product:")
    print("Your order:")
    for i in cart:
        print(i)
        print("-")*10

item = input("Enter an item:")
shopping(item)

