import os 
os.system("cls")

car_list = ["koenigsegg", "porsche", "mercedes", "ferrari"]

while True:
    print("Current Car brand List:", car_list)
    print("1. Add a car")
    print("2. Remove a car")
    print("3. Change a car")
    print("4. Exit")

    choice = input("Pick one (1/2/3/4): ")

    if choice == '1':
        item = input("Enter the car brand to add: ")
        car_list.append(item)
    elif choice == '2':
        if car_list:
            item_to_remove = input("Enter the car brand to remove: ")
            car_list.remove(item_to_remove)
        else:
            print("The list is empty.")
    elif choice == '3':
        if car_list:
            old_item = input("Enter the car brand to change: ")
            new_item = input("Enter your new car brand: ")
            if old_item in car_list:
                index = car_list.index(old_item)
                car_list[index] = new_item
            else:
                print("car brand was not found in the list.")
        else:
            print("The list is empty.")
    elif choice == '4':
        break
    else:
        print("Your choice is incorrect. Enter a correct car brand.")