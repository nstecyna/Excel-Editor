import openpyxl

def inventory(filename, wb):
    """
    Asks for a sheet and columns for the item, previous inventory counts, and
    new inventory count, and goes through each of them for new inputs for the
    new list.
    param list:
        (str) filename = the filename of the active excel document
        (Workbook) wb = a workbook of the active excel document
    """
    print("\nInventory for " + filename + ".")
    # only moves forward when sheetIn is one of the sheets in the wb
    sheetIn = ""
    while sheetIn not in wb.sheetnames:
        sheetIn = input("Please input a valid excel sheet in this document "
            + "(case-sensitive) " + str(wb.sheetnames) + ": ")
    sheet = wb[sheetIn]

    itemCol = input("Please input the column for the item names: ")
    prevCol = input("Please input the column for the previous inventory: ")
    currCol = input("Please input the column for the current inventory: ")

    for i in range(len(sheet[itemCol])):
        # only allows edits for rows with an integer in the previous
        # inventory column, so that category label rows are not edited
        # as an item
        if (isinstance(sheet[prevCol][i].value, int)):
            newInput = ""
            # we avoid the error for when newInput takes in a string that is
            # not an int
            while not newInput.isdigit():
                newInput = input(sheet[itemCol][i].value + ", Previous: "
                + str(sheet[prevCol][i].value) + ", Current: ")
            sheet[currCol][i].value = int(newInput)
        # if the item column is empty, we don't care so we just skip it
        elif (sheet[itemCol][i].value != None):
            print(sheet[itemCol][i].value)

    wb.save(filename)
    print("\nSaved Inventory.")
    print("Inventory complete!\n\n")
