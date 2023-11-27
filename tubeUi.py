import tkinter,os
from tkinter import StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji
from ttkbootstrap.scrolled import ScrolledFrame
from tube_downloader import YouTubeDownloader
from pathlib import Path
from random import sample
from player import Music


class music_bar(Music):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.status = ""
    
        f1 = ttk.LabelFrame(
            master=self.root,
            text= "currently playing".title(),
            bootstyle= INFO,
            )
        f1.pack(fill=X, side= BOTTOM)
        # f1.place(x= self.winfo_screenwidth()*0.001,y= self.winfo_screenheight()*0.29, width=self.winfo_screenwidth()*0.38)
        # f1.place_configure(width=self.winfo_screenwidth()*0.14)

        lab_img1 = ttk.Label(self.root, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
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

        self.l1 = ttk.Label(f2,text= "<NO TRACK>",font= ("",10,"bold"))
        self.l2 = ttk.Label(f2,text= "<UNKNOWN ARTIST>",font= ("",8,"bold"), foreground= "grey")
        self.l1.pack(side= "top",pady = 1.25, anchor= W)
        self.l2.pack(side= "top",anchor="w")

        # l1.bindtags("cover")
        # l2.bindtags("cover")
        # self.l3.bindtags("cover")
        # f2.bindtags("cover")

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

        self.play_btn = ttk.Button(
                    master=f1,
                    text=Emoji.get('black right-pointing triangle'),
                    bootstyle=(SUCCESS, OUTLINE),
                    # padding=10,
                    command= self.play,
                )
        self.play_btn.pack(side=RIGHT, fill=X)#, expand=YES)

        b2 =  ttk.Button(
                    master=f1,
                    text=Emoji.get('black left-pointing double triangle with vertical bar'),
                    bootstyle= (PRIMARY,LINK),
                    # padding=10,
                    # command= play,
                )
        b2.pack(side=RIGHT, pady=10)
    
    def play(self): 
        self.root.focus()
        # for wig in self.l3.winfo_children():
        #     if  "cover" in wig.bindtags():
        #         if str(wig.winfo_class()) == "TFrame":
        #             for wig1 in wig.winfo_children():
        #                 if "cover" in wig1.bindtags():
        #                     print(wig1.winfo_name())
        #                     pass
        #         print()
        #         print(wig.winfo_name())
        if self.status == "Song PLAYING" or self.status == "Song RESUMED":
            self.play_btn.configure(text= Emoji.get('black right-pointing triangle'))
        else:
            self.play_btn.configure(text= Emoji.get('double vertical bar'))
        super().resume_pause_song()
    
    def play_song(self, song_name: StringVar, songs_list):
        self.play_btn.configure(text= Emoji.get('double vertical bar'))
        self.l1.configure(text= song_name[1])
        self.l2.configure(text= song_name[0])
        return super().play_song(song_name, songs_list)

class Def_Songs(ttk.Frame):
    def __init__(self, master, nam, btt, **kwargs) -> None:
        super().__init__(master, padding= 6, bootstyle= btt, **kwargs)
        # self.pack(expand= True, fill= X,padx=10, pady=5)
        self.name = ""#"\n".join(nam.split("~"))
        self.cont1 = ttk.Frame(self, bootstyle= btt)
        self.cont1.pack(fill= X)
        self.cont2 = ttk.Frame(self, bootstyle= btt)
        self.cont2.pack(side= LEFT, expand= True, fill=X, pady=5)
        lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        self.l1 = ttk.Label(self.cont1, text= self.name, bootstyle= (btt, INVERSE), font=("bold", 8), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= (btt), text= "⁝")
        self.b3.pack(side= RIGHT, padx= 10)
        lab_img2.pack(side= LEFT, padx= 10)
        self.l1.pack(side=LEFT)

        ttk.Button(self.cont2, text= "Downlaod").pack(side= LEFT, expand= True, fill=X, padx= 5)
        ttk.Button(self.cont2, text= "Play", bootstyle= INFO).pack(side= LEFT, expand= True, fill=X, padx= 5)

    def view(self, nam):
        self.name = nam
        if self.name != "":
            self.name = "\n".join(nam.split("~"))
            self.pack(expand= True, fill= X,padx=10, pady=5)
            self.l1.configure(text= self.name)
        else:
            self.pack_forget()

class Songs(ttk.Frame):
    def __init__(self, master, nam="", **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.name = nam
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        self.l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 8), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝")
        
        self.cont1.pack(fill= X)
        lab_img2.pack(side= LEFT, padx= 10)
        self.l1.pack(side=LEFT)
        self.b3.pack(side= RIGHT, padx= 10)
        self.cont2.pack(side= RIGHT, expand= True, fill=X, padx= 10)

        ttk.Button(self.cont2, text= "Downlaod", width=10, bootstyle= INFO).pack(side= RIGHT, fill=X, padx= 10)
        ttk.Button(self.cont2, text= "Play", bootstyle= SECONDARY, width=10).pack(side= RIGHT, fill=X, padx= 10)
    
    def view(self, nam):
        self.name = nam
        if self.name != "":
            self.name = "\n".join(nam.split("~"))
            self.pack(expand= True, fill= X,padx=10, pady=5)
            self.l1.configure(text= self.name)
        else:
            self.pack_forget()

class lib_Songs(ttk.Frame):
    def __init__(self, master, nam="", path= "", music="",limt:int=18, **kwargs) -> None:
        super().__init__(master, padding= 0, **kwargs)
        self.pack(expand= True, fill= X,padx=0, pady=5, anchor= N)
        self.music = music
        self.path_name = [nam.split("~"), path]
        nam = [i if len(i) < limt else i[:limt]+".." for i in nam.split("~")]
        self.name = "\n".join(nam)
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        self.lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        
        self.lab_img2.bind("<Enter>", lambda e: self.hov(e, 0))
        self.lab_img2.bind("<Leave>", lambda e: self.hov(e, 1))
        self.lab_img2.bind("<Button-1>", self.play)
        
        self.l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 7), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝")
        
        self.cont1.pack(fill= X)
        self.lab_img2.pack(side= LEFT)
        self.l1.pack(side=LEFT, padx= 2.5)
        self.b3.pack(side= RIGHT)
        self.cont2.pack(side= RIGHT)
        ttk.Button(self.cont2, text= "⭐", bootstyle= (SECONDARY, LINK), command= lambda: self.focus()).pack(side= RIGHT)

    def hov(self,event,ty):
        if not ty:
            self.lab_img2.configure(text="▶️")
        elif ty:
            self.lab_img2.configure(text= Emoji.get("MUSICAL NOTE"))
        pass

    def play(self, event):
        name = self.path_name[0]
        path = self.path_name[1]
        self.music.play_song(name, path)

class Categories(ttk.Frame):
    def __init__(self, master, music, **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.pack(expand= True, fill= X,padx=80, pady=5)
        self.mast = ttk.Frame(self)
        cwd = [r"C:\Users\ajuga\Music", r"C:\Users\ajuga\OneDrive\Documents\Jupiter-python-try\learn\networking\musicplayer"]
        self.mast.pack(fill= X)
        self.music = music
        self.selection = ""

        self.tree = ttk.Treeview(self, selectmode= BROWSE, height= 15)
        self.tree.heading("#0", text="Song".ljust(50)+"Artist".ljust(120))
        self.tree.selection_clear()
        self.tree.bind("<Double-1>", self.play_song)
        self.tree.bind("<Button-1>", self.toggle_select)
        
        self.back = ttk.Button(self, text= "Back", bootstyle= SECONDARY, command= lambda: self.expand(0))
        self.cont1 = ttk.Frame(self.mast)
        self.cont1.pack(fill= X)
        ttk.Label(self.cont1, text= "Libary", font=("Helvetica", 13, "bold")).pack(side= LEFT)
        ttk.Button(self.cont1, text= "More", bootstyle= SECONDARY, command= lambda: self.expand(1)).pack(side= RIGHT)
        fr = [ttk.Frame(self.mast) for _ in range(3)]
        for i in range(3):
            fr[i].pack(side= LEFT, expand= True, fill=BOTH)

        # Getting songs
        if True:
            if True:
                Songs_listt = []

                for  i in cwd:
                    for folderName, _,_ in os.walk(i):
                        p = Path(folderName)
                        f = list(i for i in p.glob('*.mp3') if not i.name.startswith("verse") \
                                and str(i).split(os.sep)[3] != 'AppData'\
                                and str(i).split(os.sep)[4] != 'games')
                        if len(f) != 0:
                            Songs_listt.append(f)
                        
                tracks = []
                for i in Songs_listt:
                    for j in i:
                        j1 = [i.lstrip() for i in j.name.replace(".mp3","").split("-")]
                        if len(j1) == 1 or len(j1)>3:
                            j1 = ["UNKNOWN_ARTIST", "_".join(j1)]
                        if len(j1) == 3:
                            j2 = j1[2] if not j1[2].startswith(" ") else j1[2][1:]
                            j1 = [j2, "_".join(j1[:2])]
                        tracks.append([str(j),*j1])
                self.songtrack = tracks
            
            for j, i in enumerate(sample(tracks, 12)):
                lib_Songs(fr[j%3], "~".join(i[1:]), i[0], self.music)

    def play_song(self, event):
        item = self.tree.item(self.tree.selection())["values"]
        nam = item[2]
        pat = item[0]
        auth = item[1]
        name = (nam,auth)
        self.music.play_song(name, pat)
            # if os.path.isdir(item_path):
            #     self.cwd = item_path
            #     self.history.append(self.cwd)
            #     self.populate_tree(self.cwd)
            # self.tree.selection_clear()
            # self.show_selection()
            # self.tree.selection_set("")

    def toggle_select(self, event):
        item = self.tree.identify_row(event.y)
        if item not in self.tree.selection():
            self.tree.selection_add(item)
        else:
            self.tree.selection_remove(item)
        # self.show_selection()
        self.selected = item

    def expand(self, ty):
        if ty:
            self.mast.pack_forget()
            self.back.pack(anchor= W, pady= 5)
            self.lib(trackk= self.songtrack)
        elif not ty:
            self.lib(0)
            self.back.pack_forget()
            self.mast.pack(fill= X)
    
    def lib(self, k=1, trackk = ["",""]):
        if k:
            for i in trackk:
                self.tree.pack(fill=BOTH, expand=True)
                item_path = i[0]
                item = i[2][:20]
                itf = (30*3) - (len(item)*3)
                
                itf = " "*round(itf*0.5)
                # print(itf)
                # break
                item += itf + i[1][:20]# + i[1][:20].rjust(30)
                # print(item_path, item)
                if os.path.isfile(item_path):
                    self.tree.insert("", "end", text= item, values=(item_path, *i[1:]))
        else:
            self.tree.pack_forget()
            self.tree.selection_clear()
            self.tree.delete(*self.tree.get_children())


        

class Musicplayer(ttk.Frame):

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, padding= 10, **kwargs)
        self.pack(expand=True, fill= BOTH)
        # Usage example
        self.yt_downloader = YouTubeDownloader()
        self.search_list = ""
        self.results = []
        self.music = music_bar(self)
        # self.yt_downloader.s.run(self.yt_downloader.main1) # first connecting the app start session
        
        # self.song_list = ["hii"*(i+1) for i in range(10)]
        self.holder = "Search songs,albums,artists..."
        self.placeholder_color = "grey"
        self.default_fg_color = "white"
        
        song = "i love her eyes".title()
        author_name = "billie ellise".title()
        my_style = ttk.Style()
        my_style.configure('Link.TButton', font=("Helvetica", 15))
        

        if True: # Search
            search_frame = ttk.Frame(self)
            search_frame.pack(pady=20, fill= X, padx= 80)

            ttk.Button(search_frame,text= "<", bootstyle= SECONDARY, command= self.on_back_seach).pack(side= LEFT)

            self.search_entry = ttk.Entry(search_frame)#, width=self.winfo_screenwidth()*0.25)
            self.search_entry.pack(side=LEFT, padx=5, fill= X, expand=True)
            self.search_entry.configure(foreground= self.placeholder_color)
            self.search_entry.insert(0, self.holder)
            self.canc_sech = ttk.Button(search_frame,text= "✕", bootstyle= SECONDARY, command= self.on_cancle_search)
            # self.canc_sech.pack(side= LEFT)

            search_button = ttk.Button(search_frame, text="Search", bootstyle="info", command=self.on_search_click)
            search_button.pack(side=LEFT, padx= 5)

            self.search_entry.bind("<FocusIn>", lambda e: self.placeholder(e, 0))
            self.search_entry.bind("<FocusOut>", lambda e: self.placeholder(e, 1))
            
            self.load_bar = ttk.Progressbar(self, mode= INDETERMINATE, length= 400)

            self.container = ScrolledFrame(self, height= 430, autohide= True)
            self.lodd = ttk.LabelFrame(self.container, text= "Searched")
            # self.container.pack(fill= X)
            self.lodd.pack(fill= X, padx= 80)
            
            # Search section
            self.best_l = ttk.Label(self.lodd, text= "Best Result", font=("Helvetica", 13, "bold"))
            self.best_pick = Def_Songs(self.lodd, "", SECONDARY)
            self.oth_l = ttk.Label(self.lodd, text= "Other Songs", font=("Helvetica", 13, "bold"))
            for _ in range(5):
                self.results.append(Songs(self.lodd, ""))

            # self.create_songs_grid()

        if True: # home page
            self.cont1 = ScrolledFrame(self, height= 400)#, autohide= True)
            self.cont1.pack(expand= True, fill= BOTH)

            # ttk.Label(self.cont1, text= "Favourite", font=("Helvetica", 13, "bold")).pack() # square
            # ttk.Label(self.cont1, text= "Libary", font=("Helvetica", 13, "bold")).pack()
            Categories(self.cont1, self.music)
            # ttk.Label(self.cont1, text= "Most Played", font=("Helvetica", 13, "bold")).pack() # 
            # ttk.Label(self.cont1, text= "Albums", font=("Helvetica", 13, "bold")).pack()
            # ttk.Label(self.cont1, text= "Quick Pick", font=("Helvetica", 13, "bold")).pack()
            # ttk.Label(self.cont1, text= "Random Pick", font=("Helvetica", 13, "bold")).pack()
            pass

        if False: # bar down
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
        limit = 7
        bs = 5
        self.focus()
        if self.placeholder_color != "grey":
            # print(self.search_entry.get())
            # self.load_bar.start()
            # self.load_bar.pack()
            # self.after(5000, self.searched)

            # searching
            # result = yt_downloader.s.run(yt_downloader.main)[0]  # search result
            # songl = "\n".join(result)

            # Store for safety
            # with open("search_list", "w") as f:
            #     f.write(songl)

            # Load back
            # with open("search_list", "r") as f:
            #     result = f.read().split("\n")

            # result = result[:limit]
            # if limit < 10: bs = limit
            # tvb = threading.active_count()
            # yt_downloader.load(result, b=bs,t= tvb) # displaying

            # too = "\n".join("~".join(i) for i in yt_downloader.songlist)

            # with open("song_list", "wb") as f:
            #     f.write(too.encode())

            with open("song_list", "rb") as f:
                self.search_list = f.read().decode()
            self.search_list = [i.split("~") for i in self.search_list.split("\n")]
            
            # intiating the widgets
            self.container.pack(fill= X) # scroll contaner
            self.best_l.pack(anchor=W, padx=10, pady=10)
            self.best_pick.view(f"{self.search_list[0][0].title()[:50]}~Song ● {self.search_list[0][2]} ● 2:45")
            self.oth_l.pack(anchor=W, padx=10, pady= 10)
            for i in range(len(self.search_list))[0:5]:
                if i == 0: continue
                self.results[i].view(f"{self.search_list[i][0].title()[:50]}~Song ● {self.search_list[i][2]} ● 2:45")
            # print()#self.search_list[0][0] # song title, self.search_list[0][0] # song author

    def on_back_seach(self):
        self.focus()
        # intiating the widgets
        if self.search_list != []:
            self.search_list = []
            self.search_entry.delete(0,END)
            self.placeholder(0, 1)
            self.container.pack_forget() # scroll contaner
            # self.best_l.pack_forget()
            # self.oth_l.pack_forget()
            for i in range(len(self.search_list))[:5]:
                self.results[i].view("")

    def on_cancle_search(self):
        self.search_entry.focus()
        self.search_entry.delete(0, END)
        self.focus()
        self.canc_sech.pack_forget()

    def placeholder(self, event, ty):
        if not ty:
            self.canc_sech.pack(side= LEFT)
            if self.placeholder_color == "grey":
                self.search_entry.delete('0', 'end')
                self.search_entry.configure(foreground= self.default_fg_color)
                self.placeholder_color = self.default_fg_color
        if ty:
            if len(self.search_entry.get()) == 0:
                self.canc_sech.pack_forget()
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
