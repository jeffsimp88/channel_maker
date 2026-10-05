"""Gets various parts of an episode."""

import re

def filter_video_files(files):
    """Filter out only approved video formats"""
    video_extensions = ('.mp4', '.mkv', '.avi')
    video_files = [
        file for file in files
        if file.lower().endswith(video_extensions)
    ]
    return video_files

def check_part_three (episode, episode_files: list, match):
    """Checks if an episode has three parts."""
    is_last_file = episode_files[-1] == episode
    if is_last_file:
        return False

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
    """Checks for the other parts of an episode."""
    search_file = re.search(r'\(a\)|\(b\)|\(1\)|\(2\)|\(3\)', episode)
    if search_file:
        episode_files.sort()
        match = search_file.group()
        part_a = ""
        part_b = ""
        part_c = ""
        index = episode_files.index(episode)
        # if match == '(a)' or match == '(1)':
        if match in ('(a)','(1)'):
            part_a = f"{season}{episode}"
            part_b = f"{season}{episode_files[index + 1]}"
            if check_part_three(episode, episode_files, match):
                part_c = f"{season}{episode_files[index + 2]}"
        if match in ('(b)', '(2)'):
            part_a = f"{season}{episode_files[index - 1]}"
            part_b = f"{season}{episode}"
            if check_part_three(episode, episode_files, match):
                part_c = f"{season}{episode_files[index + 1]}"
        if match in '(3)':
            part_a = f"{season}{episode_files[index - 2]}"
            part_b = f"{season}{episode_files[index - 1]}"
            part_c = f"{season}{episode}"
        return [part_a, part_b, part_c]
    return [f"{season}{episode}"]
