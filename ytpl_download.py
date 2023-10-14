import os
from pytube import Playlist

# Function to download all videos in a playlist
def download_playlist(playlist_link, download_folder):
    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Initialize the playlist object
    playlist = Playlist(playlist_link)

    for video in playlist.videos:
        video_title = video.title
        video_file_path = os.path.join(download_folder, f"{video_title}.mp4")

        # Check if the video file already exists in the download folder
        if os.path.exists(video_file_path):
            print(f"Skipping download for: {video_title} (already downloaded)")
        else:
            print(f"Downloading: {video_title}")
            video.streams.get_highest_resolution().download(output_path=download_folder)
            print(f"Downloaded: {video_title}")

if __name__ == "__main__":
    playlist_link = input("Enter the YouTube playlist link: ")
    download_folder = "\DBMS"  # Change this to your desired download folder

    download_playlist(playlist_link, download_folder)
