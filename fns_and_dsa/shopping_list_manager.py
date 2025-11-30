# Define the function to display the menu
def display_menu():
    print("\n===== SHOPPING LIST MENU =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

# Array to store shopping list items
shopping_list = []

while True:
    # Call the display_menu function
    display_menu()

    # Choice as a NUMBER
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added.")

    elif choice == 2:
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print(f"'{item}' is not in the shopping list.")

    elif choice == 3:
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\n--- Shopping List ---")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 4.")

