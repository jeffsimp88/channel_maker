"""Creates a faux channel with episodes, bumpers, and commercials."""

import os
import random
import secrets
# import subprocess
from generate_commercials import generate_commercial_break, generate_mid_commercials
from generate_episode import  check_episode_parts, filter_video_files
from create_anthology_episode import create_anthology_episode

TV_SHOWS_PATH = '../TV Shows'
# your_shows = os.listdir(tv_shows_path)
your_shows = ['Courage the Cowardly Dog', 'Dexter\'s Laboratory', 'Ed, Edd, n Eddy',
              'Johnny Bravo', 'The Powerpuff Girls', 'Sheep in the Big City',
              'Looney Tunes', 'Tom and Jerry']
random.shuffle(your_shows)
REPEAT_SCHEDULE = 5

def pick_episode (show):
    """Chooses a random episode from the show's directory"""
    show_path = f"{TV_SHOWS_PATH}/{show}"
    selected_season = ""
    episode_files = []
    episode = ""

    show_directory = os.listdir(show_path)
    show_folders = [dir for dir in show_directory if os.path.isdir(f"{show_path}/{dir}")]
    seasons_folders = [dir for dir in show_folders
                       if "season" in dir.lower() or "volume" in dir.lower()]

    if len(seasons_folders) > 0:
        selected_season = f"{secrets.choice(seasons_folders)}/"
        files = os.listdir(f"{show_path}/{selected_season}")
        episode_files = filter_video_files(files)
        episode = secrets.choice(episode_files)
    else:
        files = [file for file in show_directory if os.path.isfile(f"{show_path}/{file}")]
        episode_files = filter_video_files(files)
        if len(episode_files) > 0:
            episode = secrets.choice(episode_files)

    final_episode_path = check_episode_parts(episode, episode_files, selected_season)
    return final_episode_path

def get_intro_bumper(show):
    """Gets the show's intro bumper."""
    bumper_path = f"./Bumpers/3 - Pre- and Post-show bumper/Cartoon Cartoons - {show}.mp4"
    if os.path.isfile(bumper_path):
        return bumper_path
    return ""

def get_up_next_bumper(next_show):
    """Get's the up next bumper"""
    bumper_path = f"./Bumpers/1 - Coming Up Next/Up Next - {next_show}.mp4"
    if os.path.isfile(bumper_path):
        return bumper_path
    return ""

def get_next_show(show, shows):
    """Get's the next show in the playlist."""
    current_show_index = shows.index(show)
    next_show = ''
    if current_show_index + 1 < len(shows):
        next_show = shows[current_show_index + 1]
    else:
        next_show = shows[0]
    return next_show

def build_episode_parts(show):
    """Builds out the episodes parts"""
    episode_block = []
    intro_bumper = get_intro_bumper(show)
    if intro_bumper:
        episode_block.append(f"{intro_bumper}\n")
    episode_parts = pick_episode(show)
    for part in episode_parts:
        if part == '':
            break
        episode_parts_2_3 = episode_parts.index(part) == 1 or episode_parts.index(part) == 2
        if len(episode_parts) > 1 and episode_parts_2_3:
            commercials = generate_mid_commercials(show)
            for clip in commercials:
                if clip:
                    episode_block.append(clip)
        episode_block.append(f"{TV_SHOWS_PATH}/{show}/{part}\n")
    return episode_block

def write_playlist(shows):
    """Writes the playlist file"""
    with open('playlist.m3u', "w", encoding="utf-8") as playlist:
        playlist.write("#EXTM3U\n")
    for _ in range(REPEAT_SCHEDULE):
        with open('playlist.m3u', "a", encoding="utf-8") as playlist:
            for show in shows:
                is_anthology_show = show == "Looney Tunes" or show == "Tom and Jerry"
                if is_anthology_show:
                    episode = create_anthology_episode(show)
                else: episode = build_episode_parts(show)

                for part in episode:
                    playlist.write(part)

                next_show = get_next_show(show, shows)
                up_next = get_up_next_bumper(next_show)
                if up_next:
                    playlist.write(f"{up_next}\n")

                commercials = generate_commercial_break()
                for clip in commercials:
                    if clip != "":
                        playlist.write(clip)

write_playlist(your_shows)
print('Your Playlist is ready!')
# subprocess.run(['vlc', 'playlist.m3u', '--fullscreen'])
