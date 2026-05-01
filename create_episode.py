import os
import re

tv_show = input("Which Show? ")
show_path = f"../TV Shows/{tv_show}"
    
def create_playlist(episodes, show_path, season_num):
    for index in range(0, len(episodes), 2):
        episode = episodes[index]
        next_episode = episodes[index+1]
        playlist_path = f"../{episode}\n../{next_episode}"
        episode_num = re.search(r'E\d{2}', episode).group()
        next_episode_num = re.search(r'E\d{2}', next_episode).group()

        with open(f"{show_path}/Playlist/{tv_show} S{season_num}{episode_num}-{next_episode_num}.m3u", "w") as playlist:
            playlist.write(f"#EXTM3U\n{playlist_path}")

folders = os.listdir(show_path)
season_folders = [dir for dir in folders if "Season" in dir]

for folder in season_folders:
    season_path = f"{show_path}/{folder}"
    files = os.listdir(season_path)
    episodes = [file for file in files if os.path.isfile(f"{season_path}/{file}")]
    season_num = season_folders.index(folder)+1
    create_playlist(episodes, season_path, season_num)