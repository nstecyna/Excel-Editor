import openpyxl

def changeValue(filename, wb, sheetName, cell):
    '''
    Changes the value of the cell on the current sheet, and saves the Workbook.
    param list:
        (str) filename = the filename of the active excel document
        (Workbook) wb = a workbook of the active excel document
        (str) sheetName = the name of the active sheet in the active wb
        (Cell) cell = the current cell which has it's value being changed
    '''

    print('\nInput "exit" to quit changing the value.')
    if (isinstance(cell.value, int)):
        newValue = ""
        while not newValue.isdigit():
            newValue = input("Input a new integer for " + str(cell.value) + ": ")
            if (newValue.lower() == "exit"):
                break
        if (newValue.lower() != "exit"):
            newValue = int(newValue)
    else:
        newValue = "0";
        while newValue.isdigit():
            newValue = input("Input a new item name for " + cell.value + ": ")
            if (newValue.lower() == "exit"):
                break

    if (str(newValue).lower() != "exit"):
        wb[sheetName][cell.column][cell.row - 1].value = newValue

        wb.save(filename)
        print("\nSaved Value to Cell.\n")
