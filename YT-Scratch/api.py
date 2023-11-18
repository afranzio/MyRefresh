import os
import time
import requests
from pytube import YouTube
import googleapiclient.errors
import google_auth_oauthlib.flow
import googleapiclient.discovery
import google_auth_oauthlib.flow
from dotenv import dotenv_values

config = dotenv_values(".env")

DOWNLOAD_PATH = "D:/CodeCode/Afranzio-Sunday/Youtube Automation/YT-Scratch/videos/downloads"
BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet&maxResults=25&q=tamil%20trending&chart=mostPopular&regionCode=IN&key="
BASE_URL_KEY = BASE_URL+config['API_KEY']


def Download(link, download_path):
    youtubeObject = YouTube(link)
    stream = youtubeObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        stream.download(download_path)
        print("Download Complete")
    else:
        print("No suitable streams found")


def main():
    api_service_name = "youtube"
    api_version = "v3"

    base_url = f"https://www.googleapis.com/{api_service_name}/{api_version}/"

    search_params = {
        'part': 'snippet',
        'maxResults': 3,
        'order': 'viewCount',
        'q': 'tamil papa song',
        'key': config['API_KEY']
    }

    response = requests.get(f"{base_url}search", params=search_params)

    if response.status_code == 200:
        data = response.json()
        for each in data['items']:
            yt_baseuri = "https://www.youtube.com/watch?v="
            yt_link = yt_baseuri+each['id']['videoId']
            Download(yt_link, DOWNLOAD_PATH)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()