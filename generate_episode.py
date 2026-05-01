import os

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