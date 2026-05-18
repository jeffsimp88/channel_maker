import os
import random
import secrets
import subprocess
from generate_commercials import generate_commercial_break, generate_mid_commercials
from generate_episode import  check_episode_parts, filter_video_files

tv_shows_path = '../TV shows'
    
def pick_episode (show):
    show_path = f"{tv_shows_path}/{show}"
    selected_season = ""
    episode_files = []
    episode = ""
    
    show_directory = os.listdir(show_path)
    show_folders = [dir for dir in show_directory if os.path.isdir(f"{show_path}/{dir}")]
    seasons_folders = [dir for dir in show_folders if "season" in dir.lower() or "volume" in dir.lower()]
   
    if len(seasons_folders) > 0:
        selected_season = f"{secrets.choice(seasons_folders)}/"
        files = os.listdir(f"{show_path}/{selected_season}")
        episode_files = filter_video_files(files)            
        episode = secrets.choice(episode_files)
    else:
        files = [file for file in show_directory if os.path.isfile(f"{show_path}/{file}")]
        episode_files = filter_video_files(files)
        if len(episode_files) > 0: episode = secrets.choice(episode_files)
    
    final_episode_path = check_episode_parts(episode, episode_files, selected_season)
    return final_episode_path

def select_bumpers(show):
    bumper_path = f"./Bumpers/3 - Pre- and Post-show bumper/Cartoon Cartoons - {show}.mp4"
    if os.path.isfile(bumper_path):
        return bumper_path
    return ""

def set_up_next_bumper(next_Show):
    bumper_path = f"./Bumpers/1 - Coming Up Next/Up Next - {next_Show}.mp4"
    if os.path.isfile(bumper_path):
        return bumper_path
    return ""

def get_next_show(show, shows):
    curent_show_index = shows.index(show)
    next_show = ''
    if curent_show_index + 1 < len(shows):
        next_show = shows[curent_show_index + 1]
    else:
        next_show = shows[0]
    return next_show

def write_playlist(shows):
    with open('playlist.m3u', "w") as playlist:
        playlist.write("#EXTM3U\n")
    for _ in range(repeat_schedule):
        with open('playlist.m3u', "a") as playlist:
            for show in shows:
                intro_bumper = select_bumpers(show)
                if intro_bumper: playlist.write(f"{intro_bumper}\n")
                
                episode_parts = pick_episode(show)
                for part in episode_parts:
                    if part == '': break
                    if len(episode_parts) > 1 and episode_parts.index(part) == 1 or episode_parts.index(part) == 2:
                        commercials = generate_mid_commercials(show)
                        for clip in commercials:
                            if clip: playlist.write(clip)
                    playlist.write(f"{tv_shows_path}/{show}/{part}\n")
                
                next_show = get_next_show(show, shows)
                up_next = set_up_next_bumper(next_show)
                if up_next: playlist.write(f"{up_next}\n")
                
                commercials = generate_commercial_break()
                for clip in commercials:
                   if clip != "": playlist.write(clip)


your_shows = ['Courage the Cowardly Dog', 'Dexter\'s Laboratory', 'Ed, Edd, n Eddy', 'Johnny Bravo', 'The Powerpuff Girls']
# your_shows = os.listdir(tv_shows_path)
random.shuffle(your_shows)
repeat_schedule = 1

write_playlist(your_shows)
print('Your Playlist is ready!')
# subprocess.run(['vlc', 'playlist.m3u', '--fullscreen'])