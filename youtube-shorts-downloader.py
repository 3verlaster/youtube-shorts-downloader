# -*- coding: utf-8 -*-
# very ezzz code
from local_lib.pytube.__main__ import YouTube as huggywuggywilleatyoucuzyouverytasty

class Developer:
    def __init__(self):
        self.name: str="Nikita"
        self.nickname: str="3verlaster"
        self.github_link: str="https://github.com/3verlaster"

def download_video_max_res(video_url):
    try:
        yt = huggywuggywilleatyoucuzyouverytasty(video_url)
        stream = yt.streams.get_highest_resolution()
        if stream:
            video_title = stream.title
            print(f"Downloading ... [{video_url}] - [{video_title.strip()}]")
            stream.download()
            return f"Video downloaded successfully."
        else:
            return "Unable to find a suitable video stream."
    except Exception as e:
        return "An error occurred: {}".format(str(e))



if __name__ == "__main__":
    developer = Developer()
    print()
    print("[GITHUB] Developer: " + developer.github_link)
    print()
    video_url = input("Type video URL here: ")
    if video_url.startswith("https://youtube.com/shorts/"): #only shorts, bro...
        response = download_video_max_res(video_url)
        print(response)
    else:
        print("This is not a youtube shorts link!")
