import os
import random
import secrets

def get_short_or_music():
    bumper_videos_paths = ["./Bumpers/CN Music Videos", "./Bumpers/CN Shorties"]
    selected_bumper = secrets.choice(bumper_videos_paths)
    video_files = os.listdir(selected_bumper)
    selected_video = [f"{selected_bumper}/{secrets.choice(video_files)}\n"]
    return selected_video

def get_commercials(num):
    commercials_path = "./Commercials"
    files = os.listdir(commercials_path)
    selected_commercials = random.sample(files, k=num)
    set_clips = [f"{commercials_path}/{clip}\n" for clip in selected_commercials] 
    return set_clips

def get_channel_bumper():
    bumper_path = "./Bumpers/2 - Station IDs"
    files = os.listdir(bumper_path)
    selected_file = [f"{bumper_path}/{secrets.choice(files)}\n"]
    return selected_file

def get_pre_post_bumpers(show, bumper_path):
    list_of_bumpers = os.listdir(bumper_path)
    show_bumpers = [file for file in list_of_bumpers if show in file]
    generic_bumpers = [file for file in list_of_bumpers if 'generic' in file.lower()]
    if len(show_bumpers) > 0:
        bumper = secrets.choice(show_bumpers)
        if os.path.isfile(f"{bumper_path}/{bumper}"): return f"{bumper_path}/{bumper}"
    if len(generic_bumpers) > 0:
        bumper = secrets.choice(generic_bumpers)
        if os.path.isfile(f"{bumper_path}/{bumper}"): return f"{bumper_path}/{bumper}"
    return ""  

def generate_mid_commercials(show):
    commercials=[]
    right_back_bumper = get_pre_post_bumpers(show, "Bumpers/5 - We_ll Be Right Back")
    commercials.extend(f"{right_back_bumper}\n")
    commercials.extend(get_commercials(3))
    back_to_bumper = get_pre_post_bumpers(show, "Bumpers/6 - Now Back To")
    commercials.extend(f"{back_to_bumper}\n")
    return commercials

def generate_commercial_break():
    commercials = []
    commercials.extend(get_short_or_music())
    commercials.extend(get_commercials(5))
    commercials.extend(get_channel_bumper())
    return commercials