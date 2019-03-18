# Favorite Song Attributes 

#refactoring code to hold variables and values as key values in a dictionary
myFavoriteSong = {"Artist": "Collective Soul", "Genre": "Alternative Rock/Pop", "Location": "Georgia", "Record Label":"Atlantic",
"Length In Minutes": 5.07, "Album": "Hints Allegations and Things Left Unsaid", "Key": "DMajor", "Release Year": 1994, "Track Number": 1,
"Written By": "Ed Roland"}
for key in myFavoriteSong:
    print(key,":", myFavoriteSong[key])

def guessMySongAttributes(key,value):
    if key in myFavoriteSong:
        if value == myFavoriteSong[key]:
            print("Correct!")
            return True
        else:
            print("Incorrect")
            return False
    else:
        print("Not a valid key")
        return False

while(True):
    for key in myFavoriteSong:
        print(key,end=" ")
    print("\nTo stop playing enter Q")
    print("Printed above is the key for attributes of my favorite song")
    key = input("type which key you would like to guess the value of?\n")
    if key == "Q" or key =="q":
        break
    else:
        guess = input("What is your guess?\n")
        guessMySongAttributes(key,guess)    
#Band information of favorite song
Artist = "Collective Soul"
Genre = "Alternative Rock/Pop"
Location = "Georgia"
RecordLabel = "Atlantic"

#Song attributes
LengthInMinutes = 5.07
Album = "Hints Allegations and Things Left Unsaid"
Key = "DMajor"
ReleaseYear = 1994
TrackNumber = 1
WrittenBy = "Ed Roland"


#print band and song attributes
'''print(Artist)
print(Genre)
print(Location)
print(RecordLabel)
print(LengthInMinutes)
print(Album)
print(Key)
print(ReleaseYear)
print(TrackNumber)
print(WrittenBy)'''
