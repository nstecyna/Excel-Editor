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
        choice = input("You can choose to: Inventory; Change Document; Exit  \n")
        if (choice.lower() in ("inventory", "i")):
            inventory.inventory(filename, wb)
            # have to refresh the wb, because we saved the info in the wb in
            # the inventory method
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
