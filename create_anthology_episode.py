"""Creates the episode of an anthology show, such as Looney Tunes or Tom & Jerry"""

import os
import secrets
from generate_episode import filter_video_files
from generate_commercials import get_commercials, get_pre_post_bumpers

def get_bumpers(show, path):
    """Gets the show's intro/outro bumpers"""
    bumper_path = f'./Bumpers/{path}'
    bumper_list = os.listdir(bumper_path)
    bumpers = [f"{bumper_path}/{file}\n" for file in bumper_list if show in file]
    print(bumpers)
    return bumpers

def get_shorts(show):
    """Gets a random short from the show."""
    show_path = f'../TV Shows/{show}'
    episode = ""
    show_directory =  os.listdir(show_path)
    show_folders = [dir for dir in show_directory if os.path.isdir(f"{show_path}/{dir}")]
    seasons_folders = [dir for dir in show_folders if "volume" or "season" in dir.lower()]

    if len(seasons_folders) > 0:
        selected_season = f"{secrets.choice(seasons_folders)}/"
        files = os.listdir(f"{show_path}/{selected_season}")
        episode_files = filter_video_files(files)
        episode = f"{show_path}/{selected_season}{secrets.choice(episode_files)}\n"
    return episode

def create_anthology_episode (show):
    """Creates the full episode with intro, shorts, bumpers, and commercials."""
    intro_path = f"./Bumpers/4 - Theme Songs/{show} - 1 Opening.mp4\n"
    outro_path = f"./Bumpers/4 - Theme Songs/{show} - 2 Closing.mp4\n"
    episode_list = [intro_path]
    for i in range(3):
        short = get_shorts(show)
        episode_list.extend([short])
        post_bumpers = get_pre_post_bumpers(show, './Bumpers/5 - We_ll Be Right Back')
        pre_bumpers = get_pre_post_bumpers(show, "./Bumpers/6 - Now Back To")
        if i < 2:
            commercials = get_commercials(3)
            episode_list.extend([post_bumpers])
            episode_list.extend(commercials)
            episode_list.extend([pre_bumpers])
    if os.path.isfile(outro_path):
        episode_list.extend([outro_path])

    return episode_list
