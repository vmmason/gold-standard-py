
import json

with open ('jukebox_list.json', 'r', encoding="utf-8") as data_file, open('premade_playlists.json', 'r', encoding="utf-8") as data_file2:
    album_library = json.load(data_file)
    premade_playlists = json.load(data_file2)

print("Thank you for using the best jukebox in the world, the Gold Standard!\nIt doesn't even play music!")

user_name = input("What's your name?  ")


def playlist_length(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def jukebox():
    start_loop = input("{}, Would you like to build a playlist, select a premade playlist, or quit? Please enter 'build', 'premade', or 'quit'.  ".format(user_name))

    user_playlist = []
    list_run_time = []


    if start_loop.upper() == "BUILD":
        requested_song_amount = int(input("Please enter the number of songs you would like to hear as a numeric digit.  "))

        for album in album_library:
            print("{} {} by {}".format(album_library.index(album)+1, album['album'], album['artist']))
        for i in range(requested_song_amount):
            choose_album = int(input("Please enter the value of the album you would like to access.  "))
            [print("{} {}".format(album_library[choose_album-1]['tracklist'].index(x)+1,x), end='\n') for x in album_library[choose_album-1]['tracklist']]
            song_choice = int(input("Enter the numeric value of your song choice.  "))-1
            user_playlist.append(song_choice)
            list_run_time.append(album_library[choose_album-1]['tracklength'][song_choice])
            #this isn't printing the value of the index, it's printing the index itself
        user_playlist = ','.join(map(str, user_playlist)) 
        print(user_playlist)
        print(playlist_length(sum(list_run_time)))

    elif start_loop.upper() == "PREMADE":
        # choose_premade = int(input("Please enter the number of the playlist you'd like to select.\n"))
        print()

        premade1 = premade_playlists[0]['premade_pl']
        premade1 = '\n'.join(premade1)
        print(premade1)

        premade2 = premade_playlists[1]['premade_pl']
        premade2 = '\n'.join(premade2)
        print(premade2)

        premade3 = premade_playlists[2]['premade_pl']
        premade3 = '\n'.join(premade3)
        print(premade3)

    elif start_loop.upper() != "QUIT":
        print("Thank you for using The Gold Standard!")

    else:
        print("Please enter 'build', 'premade', or 'quit'.")

jukebox()