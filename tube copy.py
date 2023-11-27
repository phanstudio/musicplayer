import time
import yt_dlp
from pytube import YouTube
from threading import Thread
import threading
import asyncio
from requests_html import AsyncHTMLSession
import re
import tkinter as tk
import asyncio

# loop = asyncio.get_event_loop()

# def download_ytvid_as_mp3(urll=""):
#     video_url = urll#input("enter url of youtube video:")
#     video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
#     filename = f"C:/Users/ajuga/Music/music/{video_info['title']}.mp3"#f"{video_info['title']}.mp3"
#     print(video_info["title"])

#     # options={
#     #     'format':'bestaudio/best',
#     #     'keepvideo':False,
#     #     'outtmpl':filename,
#     # }
#     # with youtube_dl.YoutubeDL(options) as ydl:
#     #     ydl.download([video_info['webpage_url']])
#     # print("Download complete... {}".format(filename))
#     pass

# def viewer(link):
#     yt = YouTube(link)
#     print(yt.title, yt.thumbnail_url, yt.author)
#     pass

# def load(li, b=5,t=1):
#     batch_size = b
#     z = round((len(li)+2)/batch_size)
#     z1 = round((len(li)/batch_size) - (len(li)//batch_size), 2)
#     print(li)

#     for j in range(z):
#         h = 0
#         if j == z-1 and len(li) % b != 0: h = round(5* (1- z1))

#         for i in li[(5*(j)):((5*(j+1))- h)]:
#             Thread(target=viewer, args=(i,), daemon= True).start()
#             time.sleep(2)

#         # for threadd in threading.enumerate():
#         #     print(threadd.name)
#         while Thread:
#             if threading.active_count() == t:
#                 break
#             pass
#         print()


# ## async
# starttime = time.time()

# def run_asyncio_coroutine(coroutine):
#     future = asyncio.run_coroutine_threadsafe(coroutine, loop)
#     future.add_done_callback(lambda f: loop.call_soon_threadsafe(tk_root.update_idletasks))

# s = AsyncHTMLSession()
# async def main(callback):
#     search_query = "billie ei".split()
#     final_query = "+".join(search_query) # add +song
#     r = await s.get('https://www.youtube.com/results?search_query={}'.format(final_query))#"https://freewebnovel.com/worlds-best-martial-artist.html")
#     # t1 = time.time()
#     # print(t1 - next_t, "sec GET", sep= "")
#     await r.html.arender(timeout= 300)
#     # t2 = time.time()
#     # print(t2 - t1, "sec RENDER", sep= "")
#     f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
#     # t3 = time.time()
#     # print(t3 - t2, "sec SELECT", sep= "")
#     f = list(map(str, f))
#     f = "\n".join(f)
#     we = re.compile(r"href='(.*)'")
#     wz = we.findall(f)
#     p = ["https://www.youtube.com"+ i for i in wz]  #https://www.youtube.com/
#     #print("done!")
#     #print(p)
#     callback(p)
#     print(p)
#     # return p
#     pass
# async def main1():
#     r = await s.get('https://www.youtube.com')#"https://freewebnovel.com/")
#     await r.html.arender(timeout= 300)
#     pass



# # print("connecting...")
# # s.run(main1)
# # next_t = time.time()
# # print(next_t - starttime, "sec ", sep= "", end= "")
# # print("connected.".upper(), "\nseaching...")
# # result = s.run(main)[0]
# # finshtime = time.time()
# # print("searched. ".upper(),finshtime - next_t, "sec", "\nshowing...", sep= "")
# def on_search_button_click():
#     run_asyncio_coroutine(main(on_search_results))

# # limit = 6
# # result = result[:limit]

# # print(result)
# # bs = 5
# # if limit < 10: bs = limit
# # tvb = threading.active_count()
# # load(result, b=bs,t= tvb)
# # tiit = time.time()
# # print(tiit - finshtime, "sec", " Done".upper(), sep= "")

# def on_search_results(results):
#     # Update your Tkinter UI with the search results, e.g., display the video titles in a listbox.
#     print(results)
#     pass


# tk_root = tk.Tk()

# search_button = tk.Button(tk_root, text="Search", command=on_search_button_click)
# search_button.pack()
# tk.Button(tk_root, text="Search0").pack()

# # Add other Tkinter widgets as needed, e.g., an entry for the search query and a listbox for the search results.

# tk_root.mainloop()



# # sync
# starttime = time.time()

# from requests_html import HTMLSession
# import re,threading


# def main():
#     search_query = "billie ei".split()
#     #print(search_query)
#     final_query = "+".join(search_query)
#     r = s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
#     # t1 = time.time()
#     # print(t1 - next_t, "sec GET", sep= "")
#     r.html.render(timeout= 300)
#     # t2 = time.time()
#     # print(t2 - t1, "sec RENDER", sep= "")
#     f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
#     # t3 = time.time()
#     # print(t3 - t2, "sec SELECT", sep= "")
#     f = list(map(str, f))
#     f = "\n".join(f)
#     we = re.compile(r"href='(.*)'")
#     wz = we.findall(f)
#     p = ["https://www.youtube.com"+ i for i in wz] #https://www.youtube.com/
#     print("done!")
#     # print(p)

# def main2():
#     r = s.get('https://www.youtube.com')
#     r.html.render(timeout= 300)
#     print(9)

# s = HTMLSession()
# print("connecting...")
# main2()

# next_t = time.time()
# print(next_t - starttime, "sec ", sep= "", end= "")
# print("Done")
# main()

# finshtime = time.time()

# print(finshtime - next_t, "sec", sep= "")


from requests_html import HTMLSession
import re,threading
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from threading import Thread
# import requests
import queue
from concurrent.futures import ThreadPoolExecutor
import asyncio
from pyppeteer import launch


class MainProcess(Thread):
    def __init__(self):#, search_query):
        super().__init__()
        # self.search_query = search_query
        self.result = None

    def run(self):

        async def fetch_and_render(url):
            browser = await launch()
            page = await browser.newPage()
            await page.goto(url)
            content = await page.content()
            await browser.close()
            return content

        def fetch_and_render_sync(url):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop.run_until_complete(fetch_and_render(url))
        
        # def fetch_and_render(url):
        #     s = HTMLSession()
        #     r = s.get(url)
        #     r.html.render(timeout=300)
        #     return r.html

        # s = HTMLSession()
        # Include your main function logic here
        # Set the result attribute with the final list of URLs
        search_query = "billie ei".split()
        #print(search_query)
        final_query = "+".join(search_query)
        url = f'https://www.youtube.com/results?search_query={final_query}'
        
        # with ThreadPoolExecutor(max_workers=1) as executor:
        #     future = executor.submit(fetch_and_render, url)
        #     html_content = future.result()
        html_content = fetch_and_render_sync(url)
        # r = s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
        # # t1 = time.time()
        # # print(t1 - next_t, "sec GET", sep= "")
        # r.html.render(timeout= 300)
        # # t2 = time.time()
        # # print(t2 - t1, "sec RENDER", sep= "")
        # f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
        # # t3 = time.time()
        # # print(t3 - t2, "sec SELECT", sep= "")
        # f = list(map(str, f))
        # f = "\n".join(f)
        # we = re.compile(r"href='(.*)'")
        # wz = we.findall(f)
        # p = ["https://www.youtube.com"+ i for i in wz] #https://www.youtube.com/
        # print("done!")
        # self.result = p#[...] # Replace this with the actual result


class App(tk.Tk):
    # ... (existing code)
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.result = tk.Text(self)  # Add this line to create the result Text widget
        self.result.pack()
        ttk.Button(self, command= self.handle_download).pack()

    def handle_download(self):
        search_query = 1#self.search_query_var.get()
        if search_query:
            # self.download_button['state'] = tk.DISABLED
            # self.result.delete(1.0, "end")
            main_process_thread = MainProcess()#search_query)
            main_process_thread.start()
            self.monitor(main_process_thread)
        else:
            showerror(title='Error', message='Please enter the search query.')

    def monitor(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread))
        else:
            # print(thread.result)
            #self.result.insert(1.0, "\n".join(thread.result))
            # self.download_button['state'] = tk.NORMAL
            pass

    # ... (existing code)

App().mainloop()
