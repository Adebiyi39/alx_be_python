def display_menu():
    print("\n===== SHOPPING LIST MENU =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def main():
    shopping_list = []  # List to hold items

    while True:
        display_menu()  # show menu

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == 2:
            # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print(f"'{item}' was not found in the shopping list.")

        elif choice == 3:
            # View items
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Shopping List ---")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == 4:
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 4.")

# Run the main function
main()
