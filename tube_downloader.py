from yt_dlp import YoutubeDL
from pytube import YouTube
from threading import Thread
import threading
import asyncio
from requests_html import AsyncHTMLSession
import re, time
# from youtube_searcher import search_youtube
# from ttkbootstrap.dialogs import Messagebox

from youtubesearchpython import VideosSearch

# # search_query = 'alan wal' + " song"
# # videos_search = VideosSearch(search_query, limit=10)

# # results = videos_search.result()

# print(*[{"title": i["title"], "length": i["duration"], "url": i["link"], "thumbnail": i["thumbnails"][0]["url"]} 
#                 for i in results["result"]], sep= "\n\n")

class YouTubeDownloader:
    def __init__(self):
        self.songlist = []
        self.prog = ''
        self.back = ''
        self.mess = []
        self.stop_event = threading.Event()
        self.thread = None
    
    def download(self,url):
        video_type = self.identify_youtube_url_type(url)
        Thread(target= self.download_manager, args=(url,video_type,self.on_progress)).start()

    def kill_thread(self):
        self.stop_event.set()
        if self.thread is not None:
            self.thread.join()
            self.thread = None

    # def create_ui(self):
    #     stop_button = tk.Button(self.root, text="Kill Thread", command=self.kill_thread)
    #     stop_button.pack()


    def on_progress(self, progress_dict):
        if progress_dict['status'] == 'downloading':
            # print(progress_dict.keys())
            progress = progress_dict['downloaded_bytes'] / progress_dict['total_bytes_estimate']
            percent = progress * 100
            # self.progress_bar.configure(value= percent)
            self.prog['value'] = percent


    def download_manager(self, url, video_type, progress_callback):
        if video_type == "playlist":
            self.download_playlist_as_mp3(url)
        elif video_type == "video":
            self.download_ytmusic_as_mp3(url,progress_callback)
        else:
            # bad formats
            ...

    def download_playlist_as_mp3(self, vid= ""):
        filename = f"playlist/" + '%(playlist_title)s/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'bestaudio/best',
            # 'extract_flat' : 'True',
            # 'dump_single_json': 'True',
            'playlist_items':"1",
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                            'nopostoverwrites': False,
                            'preferredcodec': 'mp3',
                            'preferredquality': '5'},
                            {"key": "FFmpegMetadata",
                            "add_metadata": True,},
                            {"key": "EmbedThumbnail",}],
            'outtmpl': filename,
            'ffmpeg_location': r'ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe',
            "metadata_from_title": "%(artist)s - %(title)s",
            "embed-thumbnail": True,
            "prefer_ffmpeg": True,
            "keepvideo": False,
            "writethumbnail": True,
            # "quiet": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([vid])

    def download_ytmusic_as_mp3(self, urll="",progress_callback=''):
        failed = True
        video_url = [urll]
        filename = 'music/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'bestaudio/best',
            'progress_hooks': [progress_callback],
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                            'nopostoverwrites': False,
                            'preferredcodec': 'mp3',
                            'preferredquality': '5'},
                            {"key": "FFmpegMetadata",
                            "add_metadata": True,},
                            {"key": "EmbedThumbnail",}],
            'outtmpl': filename,
            "download-archive": "downloaded_music.txt",
            'ffmpeg_location': r'./dependencies/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe',
            "metadata_from_title": "%(artist)s - %(title)s",
            "embed-thumbnail": True,
            "prefer_ffmpeg": True,
            "keepvideo": False,
            "writethumbnail": True,
            "quiet": True,
            # 'retries': 5,
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                error_code = ydl.download(video_url)
            failed = False
        except:
            ...
        if failed == True:
            self.mess.append(True)
        # print("Download complete... {}".format(filename))
        self.back.configure(state='active') # deactivate search or add to a search column

    def identify_youtube_url_type(self, url):
        video_pattern = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=[^&]+'
        playlist_pattern = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/playlist\?list=[^&]+'
        short_pattern = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/shorts\/[^&]+'

        if re.match(video_pattern, url):
            return 'video'
        elif re.match(playlist_pattern, url):
            return 'playlist'
        elif re.match(short_pattern, url):
            return 'short'
        else:
            return 'unknown'

    def search(self, query= "alan walker", retries= 2, search_lenght= 10):
        for _ in range(retries):
            worked = False
            try:
                search_query = query + " song"
                videos_search = VideosSearch(search_query, limit=search_lenght)

                results = videos_search.result()
                self.songlist = [{"title": i["title"], "length": i["duration"], "url": i["link"], "thumbnail": i["thumbnails"][0]["url"]} 
                for i in results["result"]]
                print(*self.songlist, sep="\n\n")
                worked = True
                break
            except:
                continue
        if worked == False:
            print("Error")
