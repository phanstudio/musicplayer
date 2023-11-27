# import asyncio
# from playwright.async_api import async_playwright
import time


# def sav(d): 
#     print(d)
#     with open("networking\musicplayer\sav.txt", "w", encoding= "utf-8") as f:
#         print(d)
#         d1 = "".join(d)
#         if d1 != "":
#             d = "\n".join(d)
#             #f.write(d)
#             raise ValueError()

# starttime = time.time()
# async def main():
#     async with async_playwright() as p:
#         for browser_type in [p.chromium, p.firefox, p.webkit]:
#             #async with browser_type.launch() as browser:
#             browser = await browser_type.launch()
#             page = await browser.new_page()
#             await page.goto("https://freewebnovel.com/worlds-best-martial-artist/chapter-1.html",timeout= 0)#"https://www.tigersnovel.com/content/level-up-zombie(CN)-1542-1104947/chapter-1")#"https://freewebnovel.com/son-of-the-hero-king/chapter-1.html")
#             sav(await page.locator("p").all_text_contents())
# try:
#     asyncio.run(main())
# except:
#     finshtime = time.time()

# print(finshtime - starttime)


# from requests_html import HTMLSession
# session = HTMLSession()


# starttime = time.time()

# import asyncio
# from requests_html import AsyncHTMLSession
# import re

# s = AsyncHTMLSession()
# async def main():
#     search_query = "billie ei".split()#input().split()
#     print(search_query)
#     final_query = "+".join(search_query)
#     r = await s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
#     await r.html.arender(timeout= 300)
#     f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
#     f = list(map(str, f))
#     f = await "\n".join(f)
#     we = await re.compile(r"href='(.*)'")
#     wz = await we.findall(f)
#     p = await ["https://www.youtube.com"+ i for i in wz] #https://www.youtube.com/
#     await print(p)

# s.run(main)

# finshtime = time.time()

# print(finshtime - starttime, "sec", sep= "")

import yt_dlp
from pytube import YouTube
from threading import Thread
import threading
import asyncio
from requests_html import AsyncHTMLSession
import re

# ri = ['https://www.youtube.com/watch?v=pbMwTqkKSps&list=RDQMP6WEHbxmIiY&start_radio=1', 'https://www.youtube.com/watch?v=5GJWxDKyk3A', 
# 'https://www.youtube.com/watch?v=V1Pl8CzNzCw', 'https://www.youtube.com/watch?v=SztqQQ9RDNc', 'https://www.youtube.com/watch?v=4vYOwhll1fs', 
# 'https://www.youtube.com/watch?v=pbMwTqkKSps', 'https://www.youtube.com/watch?v=viimfQi_pUw', 
# 'https://www.youtube.com/watch?v=viimfQi_pUw&list=PLcirGkCPmbmGYjUzK4XeNgbU6DTvBR7GI', 'https://www.youtube.com/watch?v=RUQl6YcMalg', 
# 'https://www.youtube.com/shorts/qhZVjtMQXLM', 'https://www.youtube.com/shorts/GAVpbsmalfE', 'https://www.youtube.com/shorts/ZN4R9rwW2NA',
#  'https://www.youtube.com/watch?v=EgBJmlPo8Xw', 'https://www.youtube.com/watch?v=gBRi6aZJGj4', 'https://www.youtube.com/watch?v=Lhf8YOdD_nE',
#   'https://www.youtube.com/watch?v=coLerbRvgsQ', 'https://www.youtube.com/watch?v=4tZ969oc-yI', 'https://www.youtube.com/watch?v=POIK1H3L86k',
#    'https://www.youtube.com/watch?v=G_BhUxx-cwk', 'https://www.youtube.com/watch?v=S2dRcipMCpw', 'https://www.youtube.com/watch?v=DyDfgMOUjCI', 
#    'https://www.youtube.com/watch?v=bsOLn1NJAco', 'https://www.youtube.com/watch?v=OORBa32WFcM', 'https://www.youtube.com/watch?v=8VLXHyHRXjc', 
#    'https://www.youtube.com/watch?v=-PZsSWwc9xA', 'https://www.youtube.com/watch?v=-tn2S3kJlyU']


def download_ytvid_as_mp3(urll=""):
    video_url = urll#input("enter url of youtube video:")
    video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"C:/Users/ajuga/Music/music/{video_info['title']}.mp3"#f"{video_info['title']}.mp3"
    print(video_info["title"])

    # options={
    #     'format':'bestaudio/best',
    #     'keepvideo':False,
    #     'outtmpl':filename,
    # }
    # with youtube_dl.YoutubeDL(options) as ydl:
    #     ydl.download([video_info['webpage_url']])
    # print("Download complete... {}".format(filename))
    pass

def viewer(link):
    yt = YouTube(link)
    print(yt.title, yt.thumbnail_url, yt.author)
    pass

def load(li, b=5,t=1):
    batch_size = b
    z = round((len(li)+2)/batch_size)
    z1 = round((len(li)/batch_size) - (len(li)//batch_size), 2)
    print(li)

    for j in range(z):
        h = 0
        if j == z-1 and len(li) % b != 0: h = round(5* (1- z1))

        for i in li[(5*(j)):((5*(j+1))- h)]:
            Thread(target=viewer, args=(i,), daemon= True).start()
            time.sleep(2)

        # for threadd in threading.enumerate():
        #     print(threadd.name)
        while Thread:
            if threading.active_count() == t:
                break
            pass
        print()


## async
starttime = time.time()



s = AsyncHTMLSession()
async def main():
    search_query = "billie ei".split()
    final_query = "+".join(search_query) # add +song
    r = await s.get('https://www.youtube.com/results?search_query={}'.format(final_query))#"https://freewebnovel.com/worlds-best-martial-artist.html")
    t1 = time.time()
    print(t1 - next_t, "sec GET", sep= "")
    await r.html.arender(timeout= 300)
    t2 = time.time()
    print(t2 - t1, "sec RENDER", sep= "")
    f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
    t3 = time.time()
    print(t3 - t2, "sec SELECT", sep= "")
    f = list(map(str, f))
    f = "\n".join(f)
    we = re.compile(r"href='(.*)'")
    wz = we.findall(f)
    p = ["https://www.youtube.com"+ i for i in wz]  #https://www.youtube.com/
    #print("done!")
    #print(p)
    return p
    pass
async def main1():
    r = await s.get('https://www.youtube.com')#"https://freewebnovel.com/")
    await r.html.arender(timeout= 300)
    pass



print("connecting...")
s.run(main1)
next_t = time.time()
print(next_t - starttime, "sec ", sep= "", end= "")
print("connected.".upper(), "\nseaching...")
result = s.run(main)[0]
finshtime = time.time()
print("searched. ".upper(),finshtime - next_t, "sec", "\nshowing...", sep= "")

limit = 6
result = result[:limit]

print(result)
# bs = 5
# if limit < 10: bs = limit
# tvb = threading.active_count()
# load(result, b=bs,t= tvb)
# tiit = time.time()
# print(tiit - finshtime, "sec", " Done".upper(), sep= "")





## sync
# starttime = time.time()

# from requests_html import HTMLSession
# import re

# s = HTMLSession()
# def main():
#     search_query = "billie ei".split()
#     #print(search_query)
#     final_query = "+".join(search_query)
#     r = s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
#     t1 = time.time()
#     print(t1 - next_t, "sec GET", sep= "")
#     r.html.render(timeout= 300)
#     t2 = time.time()
#     print(t2 - t1, "sec RENDER", sep= "")
#     f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
#     t3 = time.time()
#     print(t3 - t2, "sec SELECT", sep= "")
#     f = list(map(str, f))
#     f = "\n".join(f)
#     we = re.compile(r"href='(.*)'")
#     wz = we.findall(f)
#     p = ["https://www.youtube.com"+ i for i in wz] #https://www.youtube.com/
#     print("done!")
#     print(p)

# print("connecting...")
# r = s.get('https://www.youtube.com')
# r.html.render(timeout= 300)
# next_t = time.time()
# print(next_t - starttime, "sec ", sep= "", end= "")
# print("Done")
# main()

# finshtime = time.time()

# print(finshtime - next_t, "sec", sep= "")