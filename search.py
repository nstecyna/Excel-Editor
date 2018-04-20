import openpyxl

def search(wb, sheet, itemCol):
    '''
    Searches for cells using user input as a keyword, asks the user to choose
    one, and returns that cell.
    param list:
        (str) filename = the filename of the active excel document
        (Workbook) wb = a workbook of the active excel document
    returns:
        (Cell) cell = the cell the user wants from the search
    '''

    # a while loop so we can just restart the whole search later if conditions
    # are met
    searching = True
    while searching:
        search = input("Please input a term to search for: ")

        # search through the cells for any cells that contain the input string
        results = []
        print("Searching...")
        for cell in sheet[itemCol]:
            # TODO: make the search not pick up catagories
            if (search.lower() in str(cell.value).lower()):
                results.append(cell)

        # if we don't have any results immediately search again
        if (len(results) == 0):
            print("Found 0 results.")
            continue

        # displays the searches and an index number to select by
        print("Found " + str(len(results)) + " results:")
        for index, value in enumerate(results, start=1):
            print(str(index) + ": " + str(value.value))

        # second while loop so we can either restart this one, or go all the way
        # back to the beginning of the search process
        choosing = True
        while choosing:

            resultNum = input('Input number of choice or "new" for a new'
                + ' search: ')

            if (resultNum.lower() == 'new'):
                choosing = False
            # already checked for the string we want, so if it's still a string
            # it's not valid
            # we can also just check that the int is within our search index
            # while we're here because it's all the same output
            elif (not resultNum.isdigit() or not (0 < int(resultNum) <= len(results))):
                print("Choose a number from the list of choices.")
            # valid index in input
            else:
                cell = results[int(resultNum) - 1]
                choosing = False
                searching = False

    # we take the whole cell and not just the value in it, so we can use the
    # row, column, and change the value later.
    return cell
