import sys


# Create main menu
def MainMenu():
    while True:
        print()
        print("""### SHOPPING LIST ###
        
    Select a number for the action you would like to process: 
    
    1. View the shopping list
    2. Add an item to the shopping list
    3. Remove an item from the shopping list
    4. Check if an item is in the shopping list
    5. Check the shopping list length
    6. Clear my shopping list
    7. Exit\n""")

        selection = input("Make your selection: ")  # Asking the user to make a selection

        # Determines which action to perform depending on the user input
        if selection == "1":
            displayList()
            item1 = input("Do you wish to add more items to your shopping list?: ")
            if item1 == "y":
                item = input("Enter the item you wish to add to your shopping list: ")
                shopping_list.append(item)
                print("\n", item, "has been added to your shopping list.")
            else:
                print("\n Thanks anyways!")
                quit()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearList()
        elif selection == "7":
            sys.exit()
        else:
            print("Sorry this is not an option!")


shopping_list = ["Apples", "Bananas", "Carrots", "Potatoes"]  # Items in the shopping list to start


# Display items on the shopping lists
def displayList():
    print()
    print("--- SHOPPING LIST ---")
    for i in shopping_list:
        print("*" + i)


# Add an item to the shopping list
def addItem():
    item = input("Enter the item you wish to add to your shopping list: ")
    shopping_list.append(item)
    print(item, "has been added to your shopping list.")


# Remove an item from the shopping list
def removeItem():
    item = input("Enter the item you wish to remove from your shopping list: ")
    shopping_list.remove(item)
    print(item, "has been remove from your shopping list.")


# Check an item in the shopping list
def checkItem():
    item = input("What item would you like to check for on the shopping list?: ")
    if item in shopping_list:
        print("Yes,", item, "is in the shopping list.")
    else:
        print("No,", item, "is not on the shopping list.")


# Check how many items are on the shopping list
def listLength():
    print("There are", len(shopping_list), "items on the shopping list.")


# Clear whole list
def clearList():
    print("Your shopping list is now cleared!")
    shopping_list.clear()


MainMenu()
