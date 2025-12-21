# shopping_list_manager.py

shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' not found in the shopping list.")

    elif choice == "3":
        if shopping_list:
            print("\nCurrent Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Exiting the shopping list manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")
