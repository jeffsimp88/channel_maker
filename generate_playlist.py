import os
import random
import re
import subprocess
from generate_commercials import generateCommercialBreak, generate_mid_commercials

path = '../TV shows'

def pullEpisodes(show_dir):
    all_files = os.listdir(show_dir)
    only_folders = [dir for dir in all_files if os.path.isdir(f"{show_dir}/{dir}")]
    return only_folders

def filterVideoFiles(files):
    video_extensions = ('.mp4', '.mkv', '.avi')
    video_files = [
        file for file in files
        if file.lower().endswith(video_extensions)
    ]
    return video_files

def check_part_three (episode, episode_files: list, match):
    is_last_file = episode_files[-1] == episode
    if is_last_file: return False
    
    index = episode_files.index(episode)
    
    if match == '(b)' or match == '(2)':
        next_episode = re.search(r'\(3\)', episode_files[index + 1])
        if next_episode and next_episode.group() == '(3)':
            return True
    
    if (match == '(a)' or match == '(1)') and episode_files[-1] != episode_files[index+1]:
        next_episode = re.search(r'\(3\)', episode_files[index + 2])
        if next_episode and next_episode.group() == '(3)':
            return True
    return False

def check_episode_parts(episode, episode_files, season):
    search_file = re.search(r'\(a\)|\(b\)|\(1\)|\(2\)|\(3\)', episode)
    if search_file:
        match = search_file.group()
        part_a = ""
        part_b = ""
        part_c = ""
        index = episode_files.index(episode)
        if match == '(a)' or match == '(1)':    
            part_a = f"{season}{episode}"
            part_b = f"{season}{episode_files[index + 1]}"
            part_c = f"{season}{episode_files[index + 2]}" if check_part_three(episode, episode_files, match) else ""
        if match == '(b)' or match == '(2)':  
            part_a = f"{season}{episode_files[index - 1]}"
            part_b = f"{season}{episode}" 
            part_c = f"{season}{episode_files[index + 1]}" if check_part_three(episode, episode_files, match) else ""
        if match == '(3)':
            part_a = f"{season}{episode_files[index - 2]}"
            part_b = f"{season}{episode_files[index - 1]}"
            part_c = f"{season}{episode}"
        return [part_a, part_b, part_c]
    return [f"{season}{episode}"]
    
def pickEpisode (show):
    print(show)
    show_path = f"{path}/{show}"
    selected_season = ""
    episode_files = []
    episode = ""
    
    show_directory = os.listdir(show_path)
    show_folders = [dir for dir in show_directory if os.path.isdir(f"{show_path}/{dir}")]
    seasons_folders = [dir for dir in show_folders if "Season" in dir or "season" in dir ]
   
    if len(seasons_folders) > 0:
        selected_season = f"{random.choice(seasons_folders)}/"
        files = os.listdir(f"{show_path}/{selected_season}")
        episode_files = filterVideoFiles(files)            
        episode = random.choice(episode_files)
    else:
        files = [file for file in show_directory if os.path.isfile(f"{show_path}/{file}")]
        episode_files = filterVideoFiles(files)
        episode = random.choice(episode_files)
    
    final_episode_path = check_episode_parts(episode, episode_files, selected_season)
    return final_episode_path

def selectBumpers(show):
    bumper_path = f"./Bumpers/3 - Pre- and Post-show bumper/Cartoon Cartoons - {show}.mp4"
    if os.path.isfile(bumper_path):
        return bumper_path
    return ""

def setUpNextBumper(next_Show):
    bumper_path = f"./Bumpers/1 - Coming Up Next/Up Next - {next_Show}.mp4"
    if os.path.isfile(bumper_path):
        return bumper_path
    return ""

def get_next_show(show, shows):
    curent_show_index = shows.index(show)
    next_show = ''
    if curent_show_index+1 < len(shows):
        next_show = shows[curent_show_index+1]
    else:
        next_show = shows[0]
    return next_show

def writePlaylist(shows):
    with open('playlist.m3u', "w") as playlist:
        playlist.write("#EXTM3U\n")
    for _ in range(repeat_schedule):
        with open('playlist.m3u', "a") as playlist:
            for show in shows:
                bumper = selectBumpers(show)
                playlist.write(f"{bumper}\n")
                
                episode = pickEpisode(show)
                for part in episode:
                    if len(episode) > 1 and episode.index(part) == 1:
                        clips = generate_mid_commercials(show)
                        for clip in clips:
                            playlist.write(clip) 
                    if episode.index(part) == 2:
                        clips = generate_mid_commercials(show)
                        for clip in clips:
                            playlist.write(clip)   
                    playlist.write(f"{path}/{show}/{part}\n")
                
                next_show = get_next_show(show, shows)
                up_next = setUpNextBumper(next_show)
                playlist.write(f"{up_next}\n")
                
                commercials = generateCommercialBreak()
                for clip in commercials:
                    playlist.write(clip)


your_shows = ['Courage the Cowardly Dog', 'Dexter\'s Laboratory', 'Ed, Edd, n Eddy', 'Johnny Bravo', 'The Powerpuff Girls']
random.shuffle(your_shows)
# repeat_schedule = int(input("Number of blocks? ") or 5)
repeat_schedule = 5

writePlaylist(your_shows)
print('Your Playlist is ready!')
# subprocess.run(['vlc', 'playlist.m3u'])