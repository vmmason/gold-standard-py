
import json

with open ('jukebox_list.json', 'r', encoding="utf-8") as data_file:
    album_library = json.load(data_file)

print("Thank you for using the best jukebox in the world, the Gold Standard!\nIt doesn't even play music!")

user_name = input("What's your name?  ")


def foo():
    start_loop = input("{}, Would you like to build a playlist, select a premade playlist, or quit? Please enter 'build', 'premade', or 'quit'.  ".format(user_name))

    if start_loop.upper() != "QUIT":
        print("Thank you for using The Gold Standard!")
    elif start_loop.upper() == "BUILD":
        #Build another loop starting on this line
        for i in album_library.values('artist'):
            print("[i]{}".format('artist'))
        requested_song_amount = int(input("Please enter the number of songs you would like to hear as a numeric digit."))
        for i in (requested_song_amount):
            quit
    elif start_loop.upper() == "PREMADE":
        print("These playlists are")
    #else for when the entered value is not one of the correct values

foo

#round((x1+y1+z1)/60),0)