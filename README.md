# The Gold Standard, a Curated Jukebox

## Description

This is a simple CLI input program with a curated library of 34 albums.
It functions similarly to a real life jukebox, with options for selecting premade playlists as well.

## Features

The album library is a JSON file that is stored in a variable and accessed when the loop starts to allow you to choose your songs.
The program runs on a continuous loop as long as you don't enter "quit."
You enter the amount of songs you would like to hear, then choose from the library, and the program captures your selection to work similarly to "credits." 
After you've finished selecting, the program prints out your selection and its length by converting the sum of the seconds of each song to hh:mm:ss. 
If you would like to see the premade playlists, the program will print them out when entering the option from the menu.


## Installation

Install the repo into the directory of your choosing, and run it in your machine's terminal. The program doesn't have any dependencies and is easily ran directly from the terminal.

## Running

Run the program by navigating to the directory you choose to clone the repot in, and enter the following command into the command line. 

```
python jukebox_run.py
```

I plan to continue this and hope to add a visual aspect soon. I also would like to add an API related feature that creates a YouTube playlist. If you have any questions, comments, or general feedback, my email is `veronmmason@gmail.com`.