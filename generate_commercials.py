import os
import random

def get_short_or_music():
    bumper_videos_paths = ["./Bumpers/CN Music Videos", "./Bumpers/CN Shorties"]
    selected_bumper = random.choice(bumper_videos_paths)
    video_files = os.listdir(selected_bumper)
    selected_video = [f"{selected_bumper}/{random.choice(video_files)}\n"]
    return selected_video

def get_commercials(num):
    commercials_path = "./Commercials"
    files = os.listdir(commercials_path)
    selected_clips = random.sample(files, k=num)
    set_clips = [f"{commercials_path}/{clip}\n" for clip in selected_clips] 
    return set_clips

def get_CN_bumper():
    bumper_path = "./Bumpers/2 - Station IDs"
    files = os.listdir(bumper_path)
    selected_file = [f"{bumper_path}/{random.choice(files)}\n"]
    return selected_file

def generateCommercialBreak():
    clips = []
    clips.extend(get_short_or_music())
    clips.extend(get_commercials(5))
    clips.extend(get_CN_bumper())
    return clips

def get_right_back_bumper(show):
    bumper_path = "./Bumpers/5 - We_ll Be Right Back"
    list_of_bumpers = os.listdir(bumper_path)
    show_bumpers = [file for file in list_of_bumpers if show in file]
    bumper = random.choice(show_bumpers)
    if os.path.isfile(f"{bumper_path}/{bumper}"):
        return f"{bumper_path}/{bumper}"
    return ""

def get_back_to_bumper(show):
    bumper_path = "Bumpers/6 - Now Back To"
    list_of_bumpers = os.listdir(bumper_path)
    show_bumpers = [file for file in list_of_bumpers if show in file]
    bumper = random.choice(show_bumpers)
    if os.path.isfile(f"{bumper_path}/{bumper}"):
        return f"{bumper_path}/{bumper}"
    return ""

def generate_mid_commercials(show):
    clips=[]
    clips.extend(f"{get_right_back_bumper(show)}\n")
    clips.extend(get_commercials(3))
    clips.extend(f"{get_back_to_bumper(show)}\n")
    return clips
