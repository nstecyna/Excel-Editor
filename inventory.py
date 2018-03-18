import openpyxl

def inventory(filename, wb):
    """
    Asks for a sheet and columns for the item, previous inventory counts, and
    new inventory count, and goes through each of them for new inputs for the
    new list. Only allows edits for rows with an integer in the previous
    inventory column, so that category label rows are not edited as an item.
    param list:
        (str) filename = the filename of the active excel document
        (Workbook) wb = a workbook of the active excel document
    """
    print("\nInventory for " + filename + ".")

    print("Inventory complete!\n\n")
