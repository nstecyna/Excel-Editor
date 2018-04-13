import openpyxl

def documentCheck():
    """
    Asks for the excel filename and tries to create and returns the filename and
    a Workbook object of the file, and recurses until a valid input is input.
    returns:
        (str) excel_doc = the filename of the active excel document
        (Workbook) wb = a workbook of the active excel document
    excepts:
        IOError = an error for when using an invalid filename for a Workbook
    """
    excel_doc = input("Please enter a valid excel document name: ")
    if (excel_doc[-5:] != ".xlsx"):
        excel_doc += ".xlsx"
    try:
        wb = openpyxl.load_workbook(excel_doc)
        return excel_doc, wb
    except IOError:
        print ("Invalid document name.")
        return documentCheck()
