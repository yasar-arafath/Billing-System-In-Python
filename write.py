def over_write(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
    """
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    """
    for keys in d.keys():
        if keys == "BACON":
            L[0][2] = str(int(L[0][2])-d['BACON'])
        elif keys == "BURGER":
            L[1][2] = str(int(L[1][2])-d['BURGER'])
        elif keys == "FRIES":
            L[2][2] = str(int(L[2][2])-d['FRIES'])
        elif keys == "COKE":
            L[3][2] = str(int(L[3][2])-d['COKE'])
        elif keys == "MOMOS":
            L[4][2] = str(int(L[4][2])-d['MOMOS'])
        elif keys == "MCCAFE":
            L[5][2] = str(int(L[5][2])-d['MCCAFE'])
        else:
            L[6][2] = str(int(L[6][2])-d['PIZZA'])
    print("\nRemaining Stock Products:\n",L)
        
    files = open("products.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
