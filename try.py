from youtube_searcher import search_youtube


import threading 


def search():
    for _ in range(9):
        try:
            query = "repair a faucet tutorial".title()
            data = search_youtube(query, )
            

            print(*[{"title": i["title"], "length": i["length"], "url": i["url"], "thumbnail": i["thumbnails"][0]["url"]} 
                for i in data["videos"]][:10], sep= "\n\n")
            break
        except:
            continue


search()



# p1 = threading.Thread(target= search)

# p1.start()

# p1.join()



# from yt_dlp import YoutubeDL
# from pytube import YouTube
# from threading import Thread
# import threading
# import asyncio
# from requests_html import AsyncHTMLSession
# import re, time
# from youtube_searcher import search_youtube

# class YouTubeDownloader:
#     def __init__(self):
#         self.songlist = []
#         pass
    
#     def download(self,url):
#         video_type = self.identify_youtube_url_type(url)
#         if video_type == "playlist":
#             self.download_playlist_as_mp3(video_type)
#         elif video_type == "video":
#             self.download_ytmusic_as_mp3(video_type)
#         else:
#             # bad formats
#             ...

#     def download_playlist_as_mp3(vid= ""):
#         filename = f"playlist/" + '%(playlist_title)s/%(title)s.%(ext)s'
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             # 'extract_flat' : 'True',
#             # 'dump_single_json': 'True',
#             'playlist_items':"1",
#             'postprocessors': [{'key': 'FFmpegExtractAudio',
#                             'nopostoverwrites': False,
#                             'preferredcodec': 'mp3',
#                             'preferredquality': '5'},
#                             {"key": "FFmpegMetadata",
#                             "add_metadata": True,},
#                             {"key": "EmbedThumbnail",}],
#             'outtmpl': filename,
#             'ffmpeg_location': r'ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe',
#             "metadata_from_title": "%(artist)s - %(title)s",
#             "embed-thumbnail": True,
#             "prefer_ffmpeg": True,
#             "keepvideo": False,
#             "writethumbnail": True,
#             # "quiet": True,
#         }

#         with YoutubeDL(ydl_opts) as ydl:
#             result = ydl.download([vid])

#     def download_ytmusic_as_mp3(urll=""):
#         video_url = [urll]
#         filename = 'music/%(title)s.%(ext)s'
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'postprocessors': [{'key': 'FFmpegExtractAudio',
#                             'nopostoverwrites': False,
#                             'preferredcodec': 'mp3',
#                             'preferredquality': '5'},
#                             {"key": "FFmpegMetadata",
#                             "add_metadata": True,},
#                             {"key": "EmbedThumbnail",}],
#             'outtmpl': filename,
#             'ffmpeg_location': r'ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe',
#             "metadata_from_title": "%(artist)s - %(title)s",
#             "embed-thumbnail": True,
#             "prefer_ffmpeg": True,
#             "keepvideo": False,
#             "writethumbnail": True,
#             # "quiet": True,
#         }
#         with YoutubeDL(ydl_opts) as ydl:
#             error_code = ydl.download(video_url)
#         print("Download complete... {}".format(filename))

#     def identify_youtube_url_type(self, url):
#         video_pattern = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=[^&]+'
#         playlist_pattern = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/playlist\?list=[^&]+'
#         short_pattern = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/shorts\/[^&]+'

#         if re.match(video_pattern, url):
#             return 'video'
#         elif re.match(playlist_pattern, url):
#             return 'playlist'
#         elif re.match(short_pattern, url):
#             return 'short'
#         else:
#             return 'unknown'

#     def search(self, query= "alan walker", retries= 2, search_lenght= 10):
#         for _ in range(retries):
#             worked = False
#             try:
#                 data = search_youtube(query)
#                 self.songlist = [{"title": i["title"], "length": i["length"], "url": i["url"], "thumbnail": i["thumbnails"][0]["url"]} 
#                     for i in data["videos"]][:search_lenght]
#                 worked = True
#                 break
#             except:
#                 continue
#         if worked == False:
#             print("Error")


# v = [{'title': 'Sia - Chandelier (Official Video)', 'length': '3:52', 'url': 'https://www.youtube.com/watch?v=2vjPBrBU-TM&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/2vjPBrBU-TM/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAYu4DSMb_3qeSv7KEbARP9QNCZqQ'}, {'title': 'Sia - Unstoppable (Official Video - Live from the Nostalgic For The Present Tour)', 'length': '3:47', 'url': 'https://www.youtube.com/watch?v=YaEG2aWJnZ8&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/YaEG2aWJnZ8/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLC4ewAP1Qv1BypSmeRiUlOkM8ZCNg'}, {'title': 'SIA Greatest Hits Full Album 2023  SIA Best Songs Playlist 2023', 'length': '1:13:37', 'url': 'https://www.youtube.com/watch?v=kfM9aAdsqPE&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/kfM9aAdsqPE/hqdefault.jpg?sqp=-oaymwE2COADEI4CSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB1AaAAuADigIMCAAQARhlIGUoZTAP&rs=AOn4CLBzlj1ZfrCdXlsLA22ZxMPy0ezTNQ'}, {'title': 'Sia - Elastic Heart feat. Shia LaBeouf & Maddie Ziegler (Official Video)', 'length': '5:08', 'url': 'https://www.youtube.com/watch?v=KWZGAExj-es&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/KWZGAExj-es/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBv1mBMQVMVKeVoln9cdi8RuRfcIA'}, {'title': 'S.i.a 2023 MIX ~ Top 10 Best Songs ~ Greatest Hits ~ Full Album', 'length': '35:46', 'url': 'https://www.youtube.com/watch?v=U5kbpsFUOVU&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/U5kbpsFUOVU/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDNf0tIrTKW-8XgyL-4vzB6C41kDw'}, {'title': 'Sia - The Greatest (Official Video)', 'length': '5:52', 'url': 'https://www.youtube.com/watch?v=GKSRyLdjsPA&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/GKSRyLdjsPA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDR66JcG5b3sCnv4OGE4TcPGuA1OA'}, {'title': 'David Guetta - Titanium ft. Sia (Official Video)', 'length': '4:06', 'url': 'https://www.youtube.com/watch?v=JRfuAukYTKg&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/JRfuAukYTKg/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAJ9dZwle2HQ8icetrqJTvvaOpp3w'}, {'title': 'ZAYN - Dusk Till Dawn (Official Video) ft. Sia', 'length': '5:38', 'url': 'https://www.youtube.com/watch?v=tt2k8PGm-TI&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/tt2k8PGm-TI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBzlTrSp7XRRzjiR9hUtik9OPjYRw'}, {'title': 'Sia - Snowman [Official Video]', 'length': '2:53', 'url': 'https://www.youtube.com/watch?v=gset79KMmt0&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/gset79KMmt0/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLA-hzH8zOQLp8GjFJoqM7s7wlvwqg'}, {'title': 'Sia - Cheap Thrills (Official Lyric Video) ft. Sean Paul', 'length': '4:22', 'url': 'https://www.youtube.com/watch?v=nYh-n7EOtMA&pp=ygUDc2lh', 'thumbnail': 'https://i.ytimg.com/vi/nYh-n7EOtMA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDb6ibb9V928ERCBkZBn7ccGA_m8g'}]


# enc = "\n~\n".join(["\n".join(f"{j}~{i}" for j, i in itn.items()) for itn in v])

# dec = [{j.split("~")[0]:j.split("~")[1] for j in i.split("\n")} for i in enc.split("\n~\n")]

# import tkinter as tk
# from tkinter import ttk

# def search():
#     query = search_entry.get()
#     for child in tree.get_children():
#         item_values = tree.item(child)['values']
#         if query.lower() not in str(item_values).lower():
#             tree.detach(child)

# def undo_search():
#     for child in detached_items:
#         tree.detach(child)
#     dt = list(detached_items)
#     dt.sort()
#     for child in dt:
#         tree.reattach(child, '', tk.END)
#     # detached_items.clear()

# root = tk.Tk()

# search_entry = tk.Entry(root)
# search_entry.pack()

# search_button = tk.Button(root, text="Search", command=search)
# search_button.pack()

# undo_search_button = tk.Button(root, text="Undo Search", command=undo_search)
# undo_search_button.pack()

# tree = ttk.Treeview(root, columns=("Name", "Age"))
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")


# for i in range(10):
#     tree.insert("", tk.END, values=(f"Person {i}", 25 + i))

# tree.pack()

# detached_items = set(tree.get_children())

# root.mainloop()
