import openpyxl

def documentCheck():
    excel_doc = raw_input("Please enter a valid excel document name: ")
    excel_doc += ".xlsx"
    try:
        wb = openpyxl.load_workbook(excel_doc)
        return wb
    except IOError:
        print "Invalid document name."
