# Start with an empty shopping list
shopping_list = []

while True:
    print("\n===== SHOPPING LIST MENU =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add item
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")

    elif choice == "2":
        # Remove item
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' was not found in the shopping list.")

    elif choice == "3":
        # View list
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("\n--- Shopping List ---")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 4.")
