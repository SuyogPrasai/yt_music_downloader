# Author: Suyog Prasai
# GitHub: https://github.com/suyogprasai
# Script: YouTube Music Downloader
# Dependencies: Refer to README.md

# Imports
from pytube import YouTube, Playlist
from pathlib import Path
import time

class Downloader:

    def __init__(self):
        self.location = self.location_init()
        print(f"[INFO] Location Set: [{self.location}]")

        self.choice = self.decision()
        self.downloader = self.yt_downloader(self.location, self.choice.upper())

    def location_init(self):
        def_location = Path.home() / "music"
        while True:
            use_default = input(f"Do you want to use the default location [{def_location}]: [(y)/(n)] ").upper()
            if use_default == "Y" or use_default == "":
                location = def_location
                break
            elif use_default == "N":
                location = input("Enter the path to your desired folder: ")
                break
            else:
                print("[ERROR] Initializing the storage folder failed")
                return 1

        try:
            location = Path(location)
            if not location.exists():
                location.mkdir(parents=True, exist_ok=True)
        except:
            print("[ERROR] The path for the storage folder is incorrect")
        return str(location)

    def download_audio(self, url, path):
        try:
            yt = YouTube(
                url,
                use_oauth=True,
                allow_oauth_cache=True
            )
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream:
                audio_stream.download(output_path=path)
                print(f"[INFO] Audio [{yt.title}] downloaded successfully at [{path}].")
                return 0
            else:
                print("[ERROR] No audio stream found for the given video")
                return 1
        except Exception as e:
            print("[ERROR] An error occurred while downloading:", e)
            return 1


    def d_video(self, path):
        url = input("Enter the URL of the music video you want to download: ")
        start = time.time()
        self.download_audio(url, path)
        end = time.time()
        total_time = end - start
        print(f"\n[INFO] Audio has been downloaded at {path} in {total_time:.2f} seconds.")

    def d_playlist(self, path):
        playlist_url = input("Enter the URL of the playlist you want to download: ")
        plist = Playlist(playlist_url)
        playlist_name = plist.title
        pl_path = Path(path) / playlist_name

        if not pl_path.exists():
            pl_path.mkdir(parents=True, exist_ok=True)

        start = time.time()
        successful_downloads = 0
        failed_downloads = 0
        
        line = "========================================"
        print(f"\n{line}")
        print(f"[INFO] Downloading {len(plist)} Audio Files")
        print(f"{line}\n")
        for index, url in enumerate(plist.video_urls, start=1):
            result = self.download_audio(url, pl_path)
            if result == 0:
                successful_downloads += 1
            else:
                failed_downloads += 1
        total_songs = len(plist)
        end = time.time()
        total_time = end - start
        print(f"\n[INFO] Download summary for playlist [{playlist_name}]:")
        print(f"[Successful downloads: {successful_downloads}]")
        print(f"[Failed downloads: {failed_downloads}]")
        print(f"[Time taken: {total_time:.2f} seconds]")

    def yt_downloader(self, path, c):
        if c == "V":
            self.d_video(path)
        elif c == "P":
            self.d_playlist(path)

    def decision(self) -> str:
        while True:
            choice = input("Do you want to download a video or a playlist: [(V)/(P)] ").upper()
            if choice in ["V", "P"]:
                return choice

if __name__ == "__main__":
    program_instance = Downloader()
    pass