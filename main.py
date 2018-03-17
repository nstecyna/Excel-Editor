import openpyxl

def main():
    excel_doc = raw_input("Please enter a valid excel document name: ")
    excel_doc += ".xlsx"
    try:
        wb = openpyxl.load_workbook(excel_doc)
    except IOError:
        print "Invalid document name."



main()
