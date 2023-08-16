# YouTube Music Downloader

**Author:** Suyog Prasai  
**GitHub:** [https://github.com/suyogprasai](https://github.com/suyogprasai)  
**License:** MIT License  

## Description

This script allows you to download audio from YouTube videos and playlists. It provides a simple command-line interface to specify the location where you want to save the downloaded audio files and whether you want to download a single video or an entire playlist.

## Features

- Download audio from a single YouTube video.
- Download audio from an entire YouTube playlist.
- Option to specify the storage location for downloaded audio.
- User-friendly command-line interface.

## Dependencies

- `pytube`: A lightweight, Pythonic library for downloading YouTube videos.
- `pathlib`: A module providing classes for working with filesystem paths.
- `time`: A module for measuring execution time and adding delays.

For installation instructions, refer to the [dependencies.md](dependencies.md) file.

## How to Use

1. Clone or download this repository from GitHub.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

```shell
python3 music_downloader.py
```

4. Follow the prompts to specify the download location and choose whether to download a video or a playlist.
5. Enter the URL of the YouTube video or playlist you want to download audio from.
6. The script will download the audio files to the specified location.

## Example Usage

1. Download audio from a single YouTube video:

```shell
Do you want to download a video or a playlist: [(V)/(P)] v
Enter the URL of the music video you want to download: [YouTube Video URL]
```

2. Download audio from a YouTube playlist:

```shell
Do you want to download a video or a playlist: [(V)/(P)] p
Enter the URL of the playlist you want to download: [YouTube Playlist URL]
```

## Notes

- This script uses the `pytube` library to interact with YouTube. If you encounter any issues, make sure you have the latest version of the library installed.
- Downloading copyrighted content without proper authorization may violate YouTube's terms of service and copyright laws. Please use this script responsibly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
