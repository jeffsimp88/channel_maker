# <center> Channel Generator </center>
This application will generate a .m3u playlist that will simulate a retro channel. It will include episodes, commercials, and bumpers.
___
### How it Works
1. It will randomize the list of shows found in the TV Shows directory.
2. Picks a random season, then random episode from each show.
3. Finds the other parts of the show and puts them in order.
   * Anthology shows will randomize the shorts, such as Looney Tunes.
4. Fills the commercial breaks with random selection of station and product commercials
   * Holiday commercials are added based on the current date (i.e. Halloween or Christmas)
5. Will loop until the full episode is complete.
6. Repeats these actions for each show.

____
This application will choose the files on a specific directory tree.

Channel Generator\
├── Bumpers\
│   ├── 1 - Coming Up Next\
│   ├── 2 - Station IDs\
│   ├── 3 - Pre- and Post-show bumper\
│   ├── 4 - Theme Songs\
│   ├── 5 - We_ll Be Right Back\
│   ├── 6 - Now Back To\
│   ├── Acme Hour and Looney Tunes Show Bumpers\
│   ├── CN Ads\
│   ├── CN Music Videos\
│   ├── CN Shorties\
├── Commercials\
├── Holiday Commercials\
│   ├── Christmas\
│   └── Halloween\
├── create_anthology_episode.py
├── generate_commercials.py
├── generate_episode.py
├── generate_playlist.py
├── playlist.m3u
___
### Video Formats
The preferred file formats for videos are:
- `.mp4`
- `.mkv`
- `.avi`