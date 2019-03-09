#Python HW4 Lists

#create empty global list variables
myUniqueList = []
myLeftovers = []

#create function to add values
def addValue(a):
    #test if value is in myUniqueList already, add to myLeftovers if it is 
    #add to myUniqueList if not
    if a in myUniqueList:
        myLeftovers.append(a)
        return False
    else:
        myUniqueList.append(a)
        return True

#adding values to test function
addValue('a')
addValue('b')
addValue('a')
addValue(1)
addValue(4.5)
addValue([1,2])
addValue([1,2])
addValue('b')
addValue('a')
addValue([3,4,5])

#printing list to see if function worked
print(myUniqueList)
#print leftover list to see that works as well
print(myLeftovers)
