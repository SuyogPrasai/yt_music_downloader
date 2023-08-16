# Author: Suyog Prasai
# Github: https://github.com/suyogprasai
# Script: This script downloads music from videos
# Dependencies: Refer to dependencies.md

# Imports
from pytube import YouTube
from pytube import Playlist
from pathlib import Path
import time

class Downloader: 

    def __init__(self) -> None: 
        self.location = self.location_init()
        print(f"[INFO] Location Set: [{self.location}] ")

        self.choice = self.decision()
        self.downloader = self.yt_downloader(self.location, (self.choice).upper())

    def location_init(self) -> str: 
        self.def_location = str(Path.home() / "music") 
        while True: 
            des = input(f"Do you want to use the default location [{self.def_location}]: [(y)\(n)] ")
            des = des.upper()
            if des == "Y" or des == "":
                location = Path(self.def_location)
                break
            elif des == "N":
                location = input("Enter the path to your desired folder: ")
                location = Path(location)
                break
            else: 
                print("[ERROR] Intitializing the storage folder failed")
                return 1
        try:
            if Path.exists(location) == False: 
                Path.mkdir(location)
        except: 
            print("[ERROR] The path for the storage folder is incorrect")
        return str(location)

    def d_video(self, path):
        url = input("Enter the url of the music you want to download: ")
        start = time.time()
        self.download_audio(url, path)
        end = time.time() 
        total_time =  end - start
        total_time = f"{total_time:.2f}"
        print(f"\n[INFO] Audio has been downloaded at {path} in {total_time} seconds") 
    
    def d_playlist(self, path): 
        playlist_url = input("Enter the url of the playlist that you wnat to download: ")
        plist = Playlist(playlist_url)
        playlist_name = plist.title
        pl_path = Path(path) / playlist_name
        
        if Path.exists(pl_path) == False: 
            Path.mkdir(pl_path)
        
        start = time.time()
        for url in plist.video_urls: 
            self.download_audio(url, pl_path) 
        total_songs = len(plist)
        end = time.time()
        total_time = end - start
        total_time = f"{total_time:.2f}" 
        print(f"\n[INFO] ({total_songs}) Audio(s) have been donwloaded at [{path}] from [{playlist_name}] in {total_time} seconds")

    def download_audio(self, url, path): 
        try: 
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream: 
                audio_stream.download(output_path=path)
                print(f"[INFO] Audio [{yt.title}] downloaded successfully at [{path}]. ")
            else:
                print("[ERROR] No audio stream found for the given video.")
        except Exception as e:
            print("[ERROR] An error occurred while downloading:", e)
        
    def yt_downloader(self, path, c): 

        if c == "V": 
            # Run download video function
            self.d_video(path)
        elif c == "P": 
            # Run download playlist function
            self.d_playlist(path)

    def decision(self) -> str:
        while True: 
            choice = input("Do you want to download a video or a playlist: [(V)\(P)] ")
            choice = choice.upper()
            if choice == "V" or choice == "P": 
                return choice
                break
        return 1
if __name__ == "__main__": 
    program_instance = Downloader() 
    pass 
