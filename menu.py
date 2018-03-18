import openpyxl
import documentCheck
import inventory

def menu():
    """
    Asks for the excel filename and continuously asks for the next action,
    until the user inputs "exit".
    """
    filename, wb = documentCheck.documentCheck();
    running = True
    while (running):
        print("What would you like to do?")
        choice = input("You can choose to: Inventory; ChangeDoc; Exit  ")
        if (choice.lower() == "inventory"):
            inventory.inventory(filename, wb)
        elif (choice.lower() == "changedoc"):
            filename, wb = documentCheck.documentCheck();
        elif (choice.lower() == "exit"):
            running = False
        else:
            print("Invalid choice.")
    print("Have a nice day!")
