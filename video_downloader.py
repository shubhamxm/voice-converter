from pytube import YouTube

def download_youtube_video(video_url, output_path="."):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        video_title = yt.title
        output_file = f"{output_path}/{video_title}.mp4"
        
        stream.download(output_path)
        print(f"Video '{video_title}' downloaded as '{output_file}'")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=pTCxXZh6VyE"  # Replace with the YouTube video URL
    download_folder = "."  # Replace with your desired download folder

    download_youtube_video(youtube_url, download_folder)
