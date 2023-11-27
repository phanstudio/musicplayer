from yt_dlp import YoutubeDL
from pytube import YouTube
from threading import Thread
import threading
import asyncio
from requests_html import AsyncHTMLSession
import re, time

class YouTubeDownloader:
    def __init__(self):
        self.songlist = []
        self.s = AsyncHTMLSession() # maybe change to outside the class
        pass
    
    def download(self,url):
        video_type = self.identify_youtube_url_type(url)
        if video_type == "playlist":
            self.download_playlist_as_mp3(video_type)
        elif video_type == "video":
            self.download_ytmusic_as_mp3(video_type)
        else:
            # bad formats
            ...

    def download_playlist_as_mp3(vid= ""):
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

    def download_ytmusic_as_mp3(urll=""):
        video_url = [urll]
        filename = 'music/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'bestaudio/best',
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
            error_code = ydl.download(video_url)
        print("Download complete... {}".format(filename))

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

    def viewer(self, link):
        yt = YouTube(link)
        self.songlist.append([yt.title, yt.thumbnail_url, yt.author])

    def load(self, li, b=5, t=1):
        batch_size = b
        z = round((len(li)+2)/batch_size)
        z1 = round((len(li)/batch_size) - (len(li)//batch_size), 2)
        # print(li)

        for j in range(z):
            h = 0
            if j == z-1 and len(li) % b != 0: h = round(5* (1- z1))
            for i in li[(5*(j)):((5*(j+1))- h)]:
                Thread(target=self.viewer, args=(i,), daemon= True).start()
                time.sleep(2)
            while Thread:
                if threading.active_count() == t:
                    break
            print()

    async def main(self):
        search_query = "billie ei".split() # change
        final_query = "+".join(search_query) # add +song
        print(8)
        r = await self.s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
        await r.html.arender(timeout= 300)
        print(9)
        f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
        # f = 
        f = "\n".join(list(map(str, f)))
        we = re.compile(r"href='(.*)'")
        wz = we.findall(f)
        p = ["https://www.youtube.com"+ i for i in wz]
        return p

    async def main1(self):
        r = await self.s.get('https://www.youtube.com')
        await r.html.arender(timeout= 300)

