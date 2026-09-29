from datetime import datetime
import os
import random
import secrets

def filter_video_files(files):
    video_extensions = ('.mp4', '.mkv', '.avi')
    video_files = [
        file for file in files
        if file.lower().endswith(video_extensions)
    ]
    return video_files

def get_short_or_music():
    bumper_videos_paths = ["./Bumpers/CN Music Videos", "./Bumpers/CN Shorties"]
    selected_bumper = secrets.choice(bumper_videos_paths)
    video_files = os.listdir(selected_bumper)
    selected_video = [f"{selected_bumper}/{secrets.choice(video_files)}\n"]
    return selected_video

def get_commercials(num):
    commercials_path = "./Commercials"
    files = os.listdir(commercials_path)
    filtered_commercials = filter_video_files(files)
    selected_commercials = random.sample(filtered_commercials, k=num)
    set_clips = [f"{commercials_path}/{clip}\n" for clip in selected_commercials]
    
    station_commercial = get_station_commericals()
    set_clips.extend(station_commercial)
    random.shuffle(set_clips)
    
    current_date = datetime.now()
    if current_date.month == 10:
        set_clips.pop()
        set_clips.extend(get_holiday_commercial("Halloween"))
        random.shuffle(set_clips)
    if current_date.month == 12 and current_date.day <= 25:
        set_clips.pop()
        set_clips.extend(get_holiday_commercial("Christmas"))
        random.shuffle(set_clips)
    return set_clips

def get_station_commericals ():
    commercials_path = "./Bumpers/CN Ads"
    files = os.listdir(commercials_path)
    filtered_files = filter_video_files(files)
    selected_commercials = secrets.choice(filtered_files)
    set_clips = [f"{commercials_path}/{selected_commercials}\n"]
    return set_clips

def get_holiday_commercial(holiday):
    commercial_path = f"./Holiday Commercials/{holiday}"
    files = os.listdir(commercial_path)
    selected_commercial = [f"{commercial_path}/{secrets.choice(files)}\n"]
    return selected_commercial

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
        if os.path.isfile(f"{bumper_path}/{bumper}"): return f"{bumper_path}/{bumper}\n"
    if len(generic_bumpers) > 0:
        bumper = secrets.choice(generic_bumpers)
        if os.path.isfile(f"{bumper_path}/{bumper}"): return f"{bumper_path}/{bumper}\n"
    return ""  

def generate_mid_commercials(show):
    commercials=[]
    right_back_bumper = get_pre_post_bumpers(show, "Bumpers/5 - We_ll Be Right Back")
    commercials.extend(f"{right_back_bumper}")
    commercials.extend(get_commercials(3))
    back_to_bumper = get_pre_post_bumpers(show, "Bumpers/6 - Now Back To")
    commercials.extend(f"{back_to_bumper}")
    return commercials

def generate_commercial_break():
    commercials = []
    commercials.extend(get_short_or_music())
    commercials.extend(get_commercials(5))
    commercials.extend(get_channel_bumper())
    return commercials