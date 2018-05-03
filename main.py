import openpyxl
import documentCheck
import inventory
import searchMenu

def menu():
    """
    Asks for the excel filename and continuously asks for the next action,
    allowing the user to search the excel document, run inventory, and change
    the current documentuntil the user inputs "exit".
    """
    filename, wb = documentCheck.documentCheck();
    running = True
    while (running):
        print("\nWhat would you like to do?")
        choice = input("You can choose to: Search; Inventory; Change Document; Exit  \n")
        if (choice.lower() in ("search", "s")):
            searchMenu.searchMenu(filename, wb)
            # have to refresh the wb, because we saved the info in the wb in
            # the inventory method
            wb = openpyxl.load_workbook(filename)
        elif (choice.lower() in ("inventory", "i")):
            inventory.inventory(filename, wb)
            wb = openpyxl.load_workbook(filename)
        elif (choice.lower() in ("changedoc", "change document", "document change", "change", "document", "cd", "c", "d")):
            filename, wb = documentCheck.documentCheck();
        elif (choice.lower() in ("exit", "e")):
            running = False
        else:
            print("Invalid choice.")
    print("Have a nice day!")

def main():
    menu()

main()
