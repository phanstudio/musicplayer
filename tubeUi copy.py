import tkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji
from ttkbootstrap.scrolled import ScrolledFrame
# from ttkbootstrap.style import colorsys

# import youtube_dl
# from pytube import YouTube
# from threading import Thread
# import threading
# import asyncio
# from requests_html import AsyncHTMLSession
# import re, time

# def download_ytvid_as_mp3(urll=""):
#     video_url = urll#input("enter url of youtube video:")
#     video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
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
#         print()

# s = AsyncHTMLSession()
# async def main():
#     search_query = "billie ei".split()
#     final_query = "+".join(search_query) # add +song
#     r = await s.get('https://www.youtube.com/results?search_query={}'.format(final_query))
#     await r.html.arender(timeout= 300)
#     f = r.html.find("div#contents ytd-item-section-renderer>div#contents a#thumbnail")
#     # f = 
#     f = "\n".join(list(map(str, f)))
#     we = re.compile(r"href='(.*)'")
#     wz = we.findall(f)
#     p = ["https://www.youtube.com"+ i for i in wz]
#     return p
     
# async def main1():
#     r = await s.get('https://www.youtube.com')
#     await r.html.arender(timeout= 300)
    



# # s.run(main1) # first connecting the app start session
# # result = s.run(main)[0]  # search result
# # songl = "\n".join(result)
# # with open("search_list", "w") as f:
# #     f.write(songl)



# with open("search_list", "r") as f:
#     result = f.read().split("\n")

# limit = 7
# bs = 5
# result = result[:limit]
# if limit < 10: bs = limit
# tvb = threading.active_count()
# load(result, b=bs,t= tvb) # displaying

# with open("song_list", "w") as f:
#     f.write(songl)



# class Songs(ttk.Frame):
#     def __init__(self, master, nam, **kwargs) -> None:
#         super().__init__(master, padding= 6, **kwargs)
#         self.pack(expand= True, fill= BOTH)
#         self.name = nam +"\n" if len(nam) < 12 else nam[:12]+"\n"+nam[12:]
#         lab_img2 = ttk.Label(self, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
#                     font= ("Helvetica", 40), padding= 10)
#         lab_img2.pack()

#         l1 = ttk.Label(self, text= self.name  if len(self.name) < 20 else str(self.name[:20])+"...", bootstyle= PRIMARY, justify= CENTER)
#         l1.pack(side=BOTTOM)

class Def_Songs(ttk.Frame):
    def __init__(self, master, nam, btt, **kwargs) -> None:
        super().__init__(master, padding= 6, bootstyle= btt, **kwargs)
        self.pack(expand= True, fill= X,padx=10, pady=5)
        self.name = "\n".join(nam.split("~"))
        self.cont1 = ttk.Frame(self, bootstyle= btt)
        self.cont1.pack(fill= X)
        self.cont2 = ttk.Frame(self, bootstyle= btt)
        self.cont2.pack(side= LEFT, expand= True, fill=X, pady=5)
        lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        l1 = ttk.Label(self.cont1, text= self.name, bootstyle= (btt, INVERSE), font=("bold", 8), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= (btt), text= "⁝")
        self.b3.pack(side= RIGHT, padx= 10)
        lab_img2.pack(side= LEFT, padx= 10)
        l1.pack(side=LEFT)

        ttk.Button(self.cont2, text= "Downlaod").pack(side= LEFT, expand= True, fill=X, padx= 5)
        ttk.Button(self.cont2, text= "Play", bootstyle= INFO).pack(side= LEFT, expand= True, fill=X, padx= 5)

class Songs(ttk.Frame):
    def __init__(self, master, nam, **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.pack(expand= True, fill= X,padx=10, pady=5)
        self.name = "\n".join(nam.split("~"))
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 8), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝")
        
        self.cont1.pack(fill= X)
        lab_img2.pack(side= LEFT, padx= 10)
        l1.pack(side=LEFT)
        self.b3.pack(side= RIGHT, padx= 10)
        self.cont2.pack(side= RIGHT, expand= True, fill=X, padx= 10)

        ttk.Button(self.cont2, text= "Downlaod", width=10, bootstyle= INFO).pack(side= RIGHT, fill=X, padx= 10)
        ttk.Button(self.cont2, text= "Play", bootstyle= SECONDARY, width=10).pack(side= RIGHT, fill=X, padx= 10)

   
class Musicplayer(ttk.Frame):

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, padding= 10, **kwargs)
        self.pack(expand=True, fill= BOTH)
        self.song_list = ["hii"*(i+1) for i in range(10)]
        self.holder = "Search songs,albums,artists..."
        self.placeholder_color = "grey"
        self.default_fg_color = "white"
        
        song = "i love her eyes".title()
        author_name = "billie ellise".title()
        my_style = ttk.Style()
        my_style.configure('Link.TButton', font=("Helvetica", 15))
        

        if True:
            search_frame = ttk.Frame(self)
            search_frame.pack(pady=20, fill= X, padx= 80)

            self.search_entry = ttk.Entry(search_frame)#, width=self.winfo_screenwidth()*0.25)
            self.search_entry.pack(side=LEFT, padx=5, fill= X, expand=True)
            self.search_entry.configure(foreground= self.placeholder_color)
            self.search_entry.insert(0, self.holder)

            search_button = ttk.Button(search_frame, text="Search", bootstyle="info", command=self.on_search_click)
            search_button.pack(side=LEFT)

            self.search_entry.bind("<FocusIn>", lambda e: self.placeholder(e, 0))
            self.search_entry.bind("<FocusOut>", lambda e: self.placeholder(e, 1))
            
            self.load_bar = ttk.Progressbar(self, mode= INDETERMINATE, length= 400)

            self.container = ScrolledFrame(self, height= 230, autohide= True)
            self.lodd = ttk.LabelFrame(self.container, text= "Searched")
            self.container.pack(fill= X)
            self.lodd.pack(fill= X, padx= 80)

            # Search section
            ttk.Label(self.lodd, text= "Best Result", font=("Helvetica", 13, "bold")).pack(anchor=W, padx=10, pady=10) 
            Def_Songs(self.lodd, "Devil Doesn't Bargain ~Song • Alec Benjamin • (Un)Commentary • 2:44", SECONDARY)
            ttk.Label(self.lodd, text= "Other Songs", font=("Helvetica", 13, "bold")).pack(anchor=W, padx=10, pady= 10)
            for _ in range(4):
                Songs(self.lodd, "Devil Doesn't Bargain ~Song • Alec Benjamin • (Un)Commentary • 2:44") 
            # self.create_songs_grid()

        if True:
            f1 = ttk.LabelFrame(
                master=self,
                text= "currently playing".title(),
                bootstyle= INFO,
            )
            f1.pack(fill=X, side= BOTTOM)
            # f1.place(x= self.winfo_screenwidth()*0.001,y= self.winfo_screenheight()*0.29, width=self.winfo_screenwidth()*0.38)
            # f1.place_configure(width=self.winfo_screenwidth()*0.14)

            lab_img1 = ttk.Label(self, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 65))
            # lab_img1.pack(side= BOTTOM, anchor= W, padx=10, pady= 0)

            
            self.l3 = ttk.Frame(f1)
            self.l3.pack(side= LEFT, padx= 5, pady = 10)

            # img_path = "peter (1).png"
            # img = ttk.PhotoImage(file=img_path).subsample(4,4)
            # li1 = ttk.Label(l3,image= img)
            lab_img2 = ttk.Label(self.l3, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 25))
            lab_img2.pack(side= LEFT, anchor= W, padx=10, pady= 0)
            f2 = ttk.Frame(self.l3)
            # li1.pack(side= LEFT, padx= 5, pady= 10)
            f2.pack(side= LEFT, padx= 5, pady = 0)

            l1 = ttk.Label(f2,text= song,font= ("",10,"bold"))
            l2 = ttk.Label(f2,text= author_name,font= ("",8,"bold"), foreground= "grey")
            l1.pack(side= "top",pady = 1.25)
            l2.pack(side= "top",anchor="w")

            l1.bindtags("cover")
            l2.bindtags("cover")
            self.l3.bindtags("cover")
            f2.bindtags("cover")

            # l1.bind_class("cover", "<Enter>", self.ent)
            # l1.bind_class("cover", "<Leave>", self.ext)
            # l1.bind_class("cover", "<Button-1>", self.maximize)

            b1 = ttk.Button(
                        master=f1,
                        text=Emoji.get('black right-pointing double triangle with vertical bar'),
                        bootstyle= (PRIMARY,LINK),
                        # padding=10,
                        # command= play,
                    )
            b1.pack(side=RIGHT, pady=10)

            play_btn = ttk.Button(
                        master=f1,
                        text=Emoji.get('black right-pointing triangle'),
                        bootstyle=(SUCCESS, OUTLINE),
                        # padding=10,
                        command= self.play,
                    )
            play_btn.pack(side=RIGHT, fill=X)#, expand=YES)

            b2 =  ttk.Button(
                        master=f1,
                        text=Emoji.get('black left-pointing double triangle with vertical bar'),
                        bootstyle= (PRIMARY,LINK),
                        # padding=10,
                        # command= play,
                    )
            b2.pack(side=RIGHT, pady=10)

    def play(self): 
        self.focus()
        for wig in self.l3.winfo_children():
            if  "cover" in wig.bindtags():
                if str(wig.winfo_class()) == "TFrame":
                    for wig1 in wig.winfo_children():
                        if "cover" in wig1.bindtags():
                            print(wig1.winfo_name())
                            pass
                print()
                print(wig.winfo_name())
        # play_btn.configure(text= Emoji.get('double vertical bar'))

    def on_search_click(self):
        self.focus()
        if self.placeholder_color != "grey":
            print(self.search_entry.get())
            self.load_bar.start()
            self.load_bar.pack()
            self.after(5000, self.searched)

    def placeholder(self, event, ty):
        if not ty:
            if self.placeholder_color == "grey":
                self.search_entry.delete('0', 'end')
                self.search_entry.configure(foreground= self.default_fg_color)
                self.placeholder_color = self.default_fg_color
        if ty:
            if len(self.search_entry.get()) == 0:
                self.placeholder_color = "grey"
                self.search_entry.configure(foreground= self.placeholder_color)
                self.search_entry.insert(0, self.holder)
    
    def searched(self):
        self.load_bar.stop()
        self.load_bar.pack_forget()

    def create_songs_grid(self):
        # outer_frame = ttk.Frame(self.lodd)
        # outer_frame.pack()

        self.song_Frame = ttk.Frame(self.lodd)#outer_frame)
        self.song_Frame.pack()

        for i in range(5):
            inner_frame = ttk.Frame(self.song_Frame)
            inner_frame.pack(side='left', padx=0, pady=0)

            for j in range(2):
                song_widget = Songs(inner_frame, self.song_list[(2*i)+j]) #[:8]
                song_widget.pack(side='top', padx=0, pady=0)
    
    # def maximize(self, event):
    #     li1.pack_forget()
    #     pass

    # def ent(self, event):
    #     l1.configure(bootstyle= (SECONDARY, INVERSE))
    #     l2.configure(bootstyle= (SECONDARY, INVERSE))
    #     f2.configure(bootstyle= SECONDARY)
    #     l3.configure(bootstyle= SECONDARY)

    # def ext(self, event):
    #     l1.configure(bootstyle= DEFAULT)
    #     l2.configure(bootstyle= DEFAULT)
    #     f2.configure(bootstyle= DEFAULT)
    #     l3.configure(bootstyle= DEFAULT)

if __name__ == "__main__":
    sze = [5,3] #3,2
    scale= 200
    sze[0],sze[1] = sze[0]*scale,sze[1]*scale
    sze= tuple(sze)
    app = ttk.Window(
        themename="superhero",
        title="TubePlayer",
        # themename="vapor",
        size=sze,#(750, 450),
        resizable=(False, False),
        )
    
    Musicplayer(app)
    app.mainloop()