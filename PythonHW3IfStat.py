#Python Homework 3 If statements


def EqualityCheck(a,b,c):
    #check for any equality return true if any equality exists, false if none.
    if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
        return True
    else:
        return False
