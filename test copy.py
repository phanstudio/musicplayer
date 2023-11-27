# from ttkbootstrap.icons import Emoji
# print(Emoji.categories())

# for i in Emoji._ITEMS:
#     if i.category == "objects":
#         print(i.name, i)





# import yt_dlp
# import pyaudio
# from pydub import AudioSegment
# from pydub.playback import play
# from io import BytesIO

# def play_audio_stream(stream_url):
#     chunk = 1024
#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=audio.get_format_from_width(2), channels=2, rate=44100, output=True)
    
#     audio_data = "Lops.wav"#BytesIO()
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'wav',
#             'preferredquality': '192',
#         }],
#         'outtmpl': audio_data,
#         'ffmpeg_location': r'ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe',
#     }
    
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([stream_url])
    
#     audio_data.seek(0)
#     song = AudioSegment.from_file(audio_data, format="wav")
    
#     for chunk in song[::chunk]:
#         stream.write(chunk._data)
    
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

# video_url = 'https://www.youtube.com/watch?v=5GJWxDKyk3A&pp=ygUJYmlsbGllIGVp'
# play_audio_stream(video_url)










# import yt_dlp
# def check_for_artist(video_url=[], search_query=""): # extra feauters
#     for i in ["songs", "playlists", "albums", "song", "playlist", "album"]:
#         search_query = search_query.lower().replace(i, "").strip()
    
#     for i in video_url:
#         vid_info = []
#         video_info = yt_dlp.YoutubeDL({"no-playlist":True}).extract_info(url = i,download=False)
#         video_channel = video_info['channel'].lower().strip()
#         if search_query in video_channel or search_query == video_channel: 
#             vid_info.append(video_info['channel_id'])
#     return vid_info

# f = """https://www.youtube.com/watch?v=5GJWxDKyk3A&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=SztqQQ9RDNc&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=pbMwTqkKSps&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=V1Pl8CzNzCw&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=DyDfgMOUjCI&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=4vYOwhll1fs&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=RUQl6YcMalg&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=viimfQi_pUw&pp=ygUJYmlsbGllIGVp
# https://www.youtube.com/watch?v=EgBJmlPo8Xw&pp=ygUJYmlsbGllIGVp"""

# vid = f.split("\n")
# video_id = check_for_artist(vid, "billie")#'https://www.youtube.com/watch?v=5GJWxDKyk3A&pp=ygUJYmlsbGllIGVp', "billie song")

# for i in video_id:
#     resit = f"https://www.youtube.com/channel/{i}/releases"
#     print(resit)

# import os
# print(os.path.exists(os.path.expanduser("~")+"\Music"))



# from requests import get
# from yt_dlp import YoutubeDL

# YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

# def search(arg):
#     with YoutubeDL(YDL_OPTIONS) as ydl:
#         try:
#             get(arg)
#         except:
#             video = [i for i in ydl.extract_info(f"ytsearch:{arg}", download=False)['entries']]#['title']
#         else:
#             video = ydl.extract_info(arg, download=False)

#     return video

# print(search("billie")[0])




# import re





# import re #add to the main equation
# import aiohttp, asyncio
# from requests_html import AsyncHTMLSession

# class Searcher:
#     def __init__(self):
#         self.s = AsyncHTMLSession()
#         self.search_type="album"

#     async def main(self):
#         search_type = self.search_type 
#         search_query = "billie eilish".split()
#         final_query = "+".join(search_query)

#         # Add "song" or "album" to the search query
#         if search_type == "song":
#             final_query += "+song"
#         elif search_type == "album":
#             final_query += "+album"

#         r = await self.s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
#         await r.html.arender(timeout=300)
#         f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
#         f = "\n".join(list(map(str, f)))
#         we = re.compile(r"href='(.*)'")
#         wz = we.findall(f)
#         p = ["https://www.youtube.com" + i for i in wz]
#         return p

# searcher = Searcher()

# # For searching songs
# searcher.search_type = "song"
# songs = searcher.s.run(searcher.main)
# print("Songs:", songs[0][:5])

# # For searching albums
# searcher.search_type = "album"
# albums = searcher.s.run(searcher.main)
# print("Albums:", albums[0][:5])



# import os

# channel_name = "Billie-Eilish"
# search_query = f"ytsearch:{channel_name}"

# # Get video URLs for the search query
# os.system(f"yt-dlp --get-id --playlist-end 1 {search_query} > urls.txt")

# # Get the channel URL from the first video URL
# with open("urls.txt", "r") as f:
#     url = f.readline().strip()
# channel_url = f"https://www.youtube.com/channel/{url.split('/')[1]}"

# print(f"The channel URL for {channel_name} is {channel_url}")
import tkinter as tk
from tkinter import ttk
import yt_dlp
import threading

def download_video(url, progress_callback):
    ydl_opts = {
        'progress_hooks': [progress_callback],
    }
    for _ in range(3):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break
        except:
            continue


def on_progress(progress_dict):
    if progress_dict['status'] == 'downloading':
        progress = progress_dict['downloaded_bytes'] / progress_dict['total_bytes']
        percent = progress * 100
        progress_bar['value'] = percent

def start_download():
    url = url_entry.get()
    threading.Thread(target=download_video, args=(url, on_progress)).start()

root = tk.Tk()

url_entry = tk.Entry(root)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=start_download)
download_button.pack()

progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack()

root.mainloop()


