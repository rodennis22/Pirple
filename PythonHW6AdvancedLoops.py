#Python HW#6 Advanced Loops
#function with 2 parameters Columns and Rows (integers)

def DrawBoard(rows,columns):
    # | | | |
    #123456789
    #---------
    #check if board is too big
    if rows > 7 or columns > 60:
        return False
    #enter loop for row
    for row in range(2*rows-1):
        #if even row go into column loop
        if row%2 == 0:
            #enter column loop
            for col in range(1,2*columns):
                #if last row print space with new line
                if col == (2*columns-1):
                    print(" ")
                #if odd print space without new line
                elif col%2 != 0:
                    print(" ",end="")
                #print column line
                else:
                    print("|",end="")
        #print row of length 2*columns-1
        else:
            print("-"*(2*columns-1))            
    return True


DrawBoard(4,3)