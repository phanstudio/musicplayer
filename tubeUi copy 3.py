import tkinter,os, threading
from tkinter import DoubleVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Querybox, Messagebox
from tube_downloader import YouTubeDownloader
from pathlib import Path
from random import sample
from playeropy import Music
from PIL import Image, ImageTk
import concurrent.futures


# next part online part

class music_bar(Music):
    def __init__(self, root, mast):
        super().__init__()
        
        self.root = root
        self.status = ""
        self.song_index = 0
        self.list_name = ""
        self.mast = mast
        self.progress_var = DoubleVar()
        self.volume_var = DoubleVar()
        self.inn = False

        
    
        f1 = ttk.LabelFrame(
            master=self.root,
            text= "currently playing".title(),
            bootstyle= INFO,
            padding= 10
            )
        f1.pack(fill=X, side= BOTTOM)

        f2 = ttk.Frame(f1)
        f2.pack(padx= 5, fill= X) 
        self.elaspe = ttk.Label(f2,text= "00:00",font= ("",10,"bold"))
        self.elaspe.pack(side= LEFT, padx= 5)
        self.progress_bar = ttk.Scale(f2, variable= self.progress_var, to= 100, command= self.move_song)
        self.progress_bar.pack(fill=X, expand= True, padx=10,side= LEFT)
        self.remain = ttk.Label(f2,text= "00:00",font= ("",10,"bold"))
        self.remain.pack(padx= 5,side= LEFT)

        # self.update_progress_bar()

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
        f4 = ttk.Frame(self.l3)
        # li1.pack(side= LEFT, padx= 5, pady= 10)
        f4.pack(side= LEFT, padx= 5, pady = 0)

        self.l1 = ttk.Label(f4,text= "<NO TRACK>",font= ("",10,"bold"))
        self.l2 = ttk.Label(f4,text= "<UNKNOWN ARTIST>",font= ("",8,"bold"), foreground= "grey")
        self.l1.pack(side= "top",pady = 1.25, anchor= W)
        self.l2.pack(side= "top",anchor="w")

        # l1.bindtags("cover")
        # l2.bindtags("cover")
        # self.l3.bindtags("cover")
        # f2.bindtags("cover")

        # l1.bind_class("cover", "<Enter>", self.ent)
        # l1.bind_class("cover", "<Leave>", self.ext)
        # l1.bind_class("cover", "<Button-1>", self.maximize)

        self.mast.bind("<space>", lambda e: self.p_p_n(e,0))
        self.mast.bind("<Key-p>", lambda e: self.p_p_n(e,2))
        self.mast.bind("<Key-n>", lambda e: self.p_p_n(e,1))

        b5 =  ttk.Button(
                    master= f1,
                    text= "🔊",#Emoji.get('black left-pointing double triangle with vertical bar'),
                    bootstyle= (SECONDARY,OUTLINE),
                    # padding=10,
                    command= lambda: self.f3.place(x=f1.winfo_screenwidth()*0.34,y=0, width= 300, height= 80),
                )
        b5.pack(side=RIGHT)

        b1 = ttk.Button(
                    master=f1,
                    text=Emoji.get('black right-pointing double triangle with vertical bar'),
                    bootstyle= (PRIMARY,OUTLINE),
                    # padding=10,
                    # width= 
                    command= self.next_song,
                )
        b1.pack(side=RIGHT, padx=10)

        b4 = ttk.Button(
                    master=f1,
                    text="5"+str(Emoji.get('black right-pointing double triangle with vertical bar')),
                    bootstyle= (PRIMARY,OUTLINE),
                    # padding=10,
                    command= self.fast_forward,
                )
        b4.pack(side=RIGHT)

        self.play_btn = ttk.Button(
                    master=f1,
                    text=Emoji.get('black right-pointing triangle'),
                    bootstyle=(SUCCESS, OUTLINE),
                    padding=10,
                    command= self.play,
                )
        self.play_btn.pack(side=RIGHT, fill=X, padx= 5)#, expand=YES)

        b3 =  ttk.Button(
                    master=f1,
                    text=str(Emoji.get('black left-pointing double triangle with vertical bar'))+"5",
                    bootstyle= (PRIMARY,OUTLINE),
                    # padding=10,
                    command= self.rewind_back,
                )
        b3.pack(side=RIGHT)

        b2 =  ttk.Button(
                    master=f1,
                    text=Emoji.get('black left-pointing double triangle with vertical bar'),
                    bootstyle= (PRIMARY,OUTLINE),
                    # padding=10,
                    command= self.previous_song,
                )
        b2.pack(side=RIGHT, padx= 10)

        self.f3 = ttk.Labelframe(f1, text= "Volume", padding=10)
        # self.f3.place(x=f1.winfo_screenwidth()*0.35,y=0, width= 300, height= 80)
        ttk.Label(self.f3, text= "🔊").pack(padx=5, side= LEFT)
        ttk.Scale(self.f3, length= 200, variable= self.volume_var, to=10, command= self.change_volume).pack(side= LEFT)
        self.volume_var.set(10.0)
        self.fig = ttk.Label(self.f3, text= f"{100}")
        self.fig.pack(padx=5, side= LEFT)
        self.mast.bind("<Button-1>", self.vol)
        self.f3.bind("<Enter>", lambda e: self.ex_ent(e, 1))
        self.f3.bind("<Leave>", lambda e: self.ex_ent(e, 0))

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
    
    def play_song(self, name):
        self.play_btn.configure(text= Emoji.get('double vertical bar'))
        song_name = name.split(";'")[1].split("~")
        self.l1.configure(text= song_name[1])
        self.l2.configure(text= song_name[0])
        self.song_index = self.playlist[self.list_name].index(name) # may be the issue
        # print(song_name)
        return super().play_song()
    
    def p_p_n(self,event,ty=0):
        if ty == 0:
            self.play()
        elif ty == 1:
            self.next_song()
        elif ty == 2:
            self.previous_song()

    def vol(self,event):
        if not self.inn:
            # self.root.focus()
            self.f3.place_forget()

    def ex_ent(self,event,tr):
        if tr:
            self.inn = True
        else:
            self.inn = False


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
    
    def play(self):
        # play a sample of the song
        # and show other suggestions
        ...
    
    def download(self):
        # add the download function here
        ...
        pass

class lib_Songs(ttk.Frame):
    def __init__(self, master, nam="", path= "", music="",limt:int=16, **kwargs) -> None:
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
            self.lab_img2.configure(text=" "+str(Emoji.get('black right-pointing triangle'))+" ")#"▶️")
        elif ty:
            self.lab_img2.configure(text= Emoji.get("MUSICAL NOTE"))
        pass

    def play(self, event):
        name = self.path_name[0]#"~".join(self.path_name[0])
        path = self.path_name[1]
        item = ";'".join((path,"~".join(name)))
        # self.music.playlist["track1"].index()
        # print(self.music.playlist["track1"])
        self.music.list_name = "track1"
        self.music.play_song(item)

class plist_Songs(ttk.Frame):
    def __init__(self, master, music="", limt:int=16, **kwargs) -> None:
        super().__init__(master, padding= 0, **kwargs)
        self.pack(expand= True, fill= X,padx=0, pady=5, anchor= N)
        self.music = music
        self.view()
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        
        self.l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 7), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝") # change to delete
        
        self.cont1.pack(fill= X)
        # self.lab_img2.pack(side= LEFT)
        self.l1.pack(side=LEFT, padx= 2.5)
        self.b3.pack(side= RIGHT)
        self.cont2.pack(side= RIGHT)
        ttk.Button(self.cont2, text= "⭐", bootstyle= (SECONDARY, LINK), command= lambda: self.focus()).pack(side= RIGHT)
        ttk.Button(self.cont2, text=" "+str(Emoji.get('black right-pointing triangle'))+" ", 
                   bootstyle= (SECONDARY, LINK), command= self.play).pack(side= RIGHT)

    def view(self, nam="", path="", vie=""):
        self.name = nam
        if self.name != "":
            self.path_name = [nam.split("~")]+[path]
            self.music.list_name = vie
            # print(self.path_name)
            self.name = "\n".join(nam.split("~"))
            self.pack(expand= True, fill= X, padx=10, pady=5)
            self.l1.configure(text= self.name)
        else:
            self.pack_forget()

    def play(self):
        name = self.path_name[0]#"~".join(self.path_name[0])
        path = self.path_name[1]
        # print(name, path)
        item = ";'".join((path,"~".join(name)))
        # self.music.playlist["track1"].index()
        # print(self.music.playlist["track1"])
        self.music.play_song(item)
        
        # self.music.playlist["track1"].append("rand%5")

class Ply_Songs(ttk.Frame):
    def __init__(self, master, nam="", img_path="", paths= [],
                 music="", mast="", sel="",limt:int=16, **kwargs) -> None:
        super().__init__(master, padding= 0, **kwargs)
        self.pack(expand= True, fill= X, padx=0, pady=5, anchor= N)
        self.music = music
        self.masters = mast
        self.sel = sel
        self.pth = paths
        # self.masters = master
        self.name = nam[:limt].upper()
        self.name = self.name + "  "*(limt - len(self.name))
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)

        def resize_image(img_path, size):
            img = Image.open(img_path)
            img.thumbnail(size)
            return img

        # img_path = "your_image_path.jpg"
        size = (100, 100)  # Desired width and height

        img = resize_image(img_path, size)
        img = ttk.PhotoImage(file=img_path).subsample(2,2)
        # li1 = ttk.Label(self.cont1,image= img)
        # li1.pack()
        self.lab_img2 = ttk.Label(self.cont1, image= img, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 35), padding= 10, compound= CENTER)
        self.lab_img2.image = img
        
        self.lab_img2.bind("<Enter>", lambda e: self.hov(e, 0))
        self.lab_img2.bind("<Leave>", lambda e: self.hov(e, 1))
        self.lab_img2.bind("<Button-1>", self.play)
        
        self.l1 = ttk.Label(self.cont2, text= self.name, font=("bold", 7), justify= LEFT, bootstyle= INVERSE)
        # self.b3 = ttk.Button(self.cont2, bootstyle= LINK, text= "⁝")
        
        self.cont1.pack(fill= X)
        self.lab_img2.pack()
        self.l1.pack(side=LEFT, pady= 2.5)
        # self.b3.pack(side= RIGHT, fill= X)
        self.cont2.pack(side= BOTTOM)
        # ttk.Button(self.cont2, text= "⭐", bootstyle= (SECONDARY, LINK), command= lambda: self.focus()).pack(side= RIGHT)

    def hov(self,event,ty):
        if not ty:
            self.lab_img2.configure(text=" "+str(Emoji.get('black right-pointing triangle'))+" ")
        elif ty:
            self.lab_img2.configure(text= Emoji.get("MUSICAL NOTE"))
        pass

    def play(self, event):
        self.masters(ty=1, pth= self.pth, vie= self.name)
        # name = self.path_name[0]#"~".join(self.path_name[0])
        # path = self.path_name[1]
        # item = ";'".join((path,"~".join(name)))
        # # self.music.playlist["track1"].index()
        # # print(self.music.playlist["track1"])
        # self.music.list_name = "track1"
        # self.music.play_song(item)
        
        # self.music.playlist["track1"].append("rand%5")
    


class Categories(ttk.Frame):
    def __init__(self, master, music, sel, **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.pack(expand= True, fill= X,padx=80, pady=5)
        self.masters = master
        self.sel = sel
        self.mast = ttk.Frame(self)
        cwd = [r"C:\Users\ajuga\Music", r"C:\Users\ajuga\OneDrive\Documents\Jupiter-python-try\learn\networking\musicplayer"]
        self.mast.pack(fill= X)
        self.music = music
        self.selection = ""
        self.view = "ui"

        self.tree = ttk.Treeview(self.sel, selectmode= BROWSE, height= 13)
        self.tree.heading("#0", text="Song".ljust(50)+"Artist".ljust(120))
        self.tree.selection_clear()
        self.tree.bind("<Double-1>", self.play_song)
        self.tree.bind("<Button-1>", self.toggle_select)
        
        self.back = ttk.Button(self.sel, text= "Back", bootstyle= SECONDARY, command= lambda: self.expand(0))
        self.cont1 = ttk.Frame(self.mast)
        self.cont1.pack(fill= X)
        ttk.Label(self.cont1, text= "Libary", font=("Helvetica", 13, "bold")).pack(side= LEFT)
        ttk.Button(self.cont1, text= "More", bootstyle= SECONDARY, command= lambda: self.expand(1)).pack(side= RIGHT)
        ttk.Button(self.cont1, text= "↻", bootstyle= (LINK), command= self.refresh).pack(side= RIGHT)
        ttk.Button(self.cont1, text= "+", bootstyle= (LINK), command= self.add_to).pack(side= RIGHT)
        self.fr = [ttk.Frame(self.mast) for _ in range(3)]
        for i in range(3):
            self.fr[i].pack(side= LEFT, expand= True, fill=BOTH)

        # Getting songs
        if True:
            if True:
                Songs_listt1 = []
                Songs_listt2 = []
                Songs_listt = []

                for  i in cwd:
                    for folderName, _,_ in os.walk(i):
                        p = Path(folderName)
                        f = list(i for i in p.glob('*.mp3') if not i.name.startswith("verse") \
                                and str(i).split(os.sep)[3] != 'AppData'\
                                and str(i).split(os.sep)[4] != 'games')
                        if len(f) != 0:
                            Songs_listt1.append(f)
                for  i in cwd:
                    for folderName, _,_ in os.walk(i):
                        p = Path(folderName)
                        f = list(i for i in p.glob('*.wav') if not i.name.startswith("verse") \
                                and str(i).split(os.sep)[3] != 'AppData'\
                                and str(i).split(os.sep)[4] != 'games')
                        if len(f) != 0:
                            Songs_listt2.append(f)
                
                Songs_listt = Songs_listt1 + Songs_listt2
                        
                tracks = []
                for i in Songs_listt:
                    for j in i:
                        j1 = [i.lstrip() for i in j.name.replace(".mp3","").replace(".wav","").split("-")]
                        if len(j1) == 1 or len(j1)>3:
                            j1 = ["UNKNOWN_ARTIST", "_".join(j1)]
                        if len(j1) == 3:
                            j2 = j1[2] if not j1[2].startswith(" ") else j1[2][1:]
                            j1 = [j2, "_".join(j1[:2])]
                        tracks.append([str(j),*j1])
                self.songtrack = tracks
            self.music.playlist["track1"] = []
            self.libb =[]
            for j, i in enumerate(sample(tracks, 12)):
                self.libb.append(lib_Songs(self.fr[j%3], "~".join(i[1:]), i[0], self.music))
                self.music.playlist["track1"].append(";'".join((i[0], "~".join(i[1:]))))
            # print(self.music.playlist)

    def play_song(self, event):
        item = self.tree.item(self.tree.selection())["values"]
        nam = item[2]
        path = item[0]
        auth = item[1]
        name = (auth,nam)
        item = ";'".join((path,"~".join(name)))
        self.music.list_name = "track2"
        self.music.play_song(item)
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
            self.view = "li"
            self.masters.pack_forget()
            self.back.pack(anchor= W, pady= 5)
            self.lib(trackk= self.songtrack)
        elif not ty:
            self.view = "ui"
            self.lib(0)
            self.back.pack_forget()
            self.masters.pack(fill= X)
    
    def lib(self, k=1, trackk = ["",""]):
        if k:
            self.music.playlist["track2"] = []
            for i in trackk:
                self.tree.pack(fill=BOTH, expand=True)
                item_path = i[0]
                item = i[2][:20].ljust(30) + i[1][:20].rjust(30)
                # print(item_path, item)
                if os.path.isfile(item_path):
                    self.tree.insert("", "end", text= item, values=(item_path, *i[1:]))
                    self.music.playlist["track2"].append(";'".join((i[0], "~".join(i[1:]))))
        else:
            self.tree.pack_forget()
            self.tree.selection_clear()
            self.tree.delete(*self.tree.get_children())

    def refresh(self):
        self.focus()
        for i in self.libb:
            i.destroy()
        self.music.playlist["track1"] = [] # refresh
        for j, i in enumerate(sample(self.songtrack, 12)):
            self.libb.append(lib_Songs(self.fr[j%3], "~".join(i[1:]), i[0], self.music))
            self.music.playlist["track1"].append(";'".join((i[0], "~".join(i[1:]))))
        ...

    def add_to(self): # add an input
        # Query box
        self.focus()
        try:
            query = Querybox.get_string("Name the new Playlist", "PlaylistNamer")
            if query == "":
                raise("Cancle the entry, or add a name Error")
        except:
            Messagebox.show_error("Cancle the entry, or add a name")
            query = None
        if query != None:
            name = f"{query}(list).txt"
            for i in range(20):
                if not os.path.exists(f"dependencies\\custom_playlist\\{name}"):
                    break
                name = f"{query}-{i+1}(list).txt"
            with open(f"dependencies\\custom_playlist\\{name}", "wb") as f:
                f.write(
                ("imgs\peter (1).png\n"+ #place holder until image gotten # NAN
                "\n".join(i.split(";")[0] for i in self.music.playlist["track1"])).encode()
                )
            li = [name.replace("(list).txt", ""), "imgs\peter (1).png", [i.split(";")[0] for i in self.music.playlist["track1"]]]
            lenn = len(self.sel.pl_cat.libb)
            self.sel.pl_cat.Play_list.append(li)
            if lenn < 10:
                self.sel.pl_cat.libb.append(Ply_Songs(self.sel.pl_cat.fr[(lenn)%5], *li
                                                    ,self.sel.pl_cat.music, self.sel.pl_cat.expand, self.sel))
        ...

class Playlist_Cat(ttk.Frame):
    # Add no playlist
    def __init__(self, master, music, sel, **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.pack(expand= True, fill= X,padx=80, pady=5)
        self.masters = master
        self.rev = 1
        self.mast = ttk.Frame(self, bootstyle= SECONDARY)
        cwd_music = os.path.expanduser("~")+"\Music"
        cwd = [cwd_music, r"./"] # fix
        self.mast.pack(fill= X)
        self.music = music
        
        self.back = ttk.Button(sel, text= "Back", bootstyle= SECONDARY, command= lambda: self.expand(0))
        self.tree = ttk.Treeview(sel, selectmode= BROWSE, height= 13)
        self.tree.heading("#0", text="Playlist", anchor= "w")
        self.tree.selection_clear()
        self.tree.bind("<Double-1>", self.play_song)
        self.tree.bind("<Button-1>", self.toggle_select)

        self.cont1 = ttk.Frame(self.mast)
        self.cont1.pack(fill= X)
        ttk.Label(self.cont1, text= "Playlist", font=("Helvetica", 13, "bold")).pack(side= LEFT)
        ttk.Button(self.cont1, text= "More", bootstyle= SECONDARY, command= self.expance).pack(side= RIGHT) # to mange more playlist
        # ttk.Button(self.cont1, text= "↻", bootstyle= (LINK), command= self.refresh).pack(side= RIGHT)
        self.fr = [ttk.Frame(self.mast) for _ in range(5)]
        for i in range(5):
            self.fr[i].pack(side= LEFT, expand= True, fill=BOTH)

        self.rrf = ScrolledFrame(sel, height= 400)
        self.pl_list = []
        for _ in range(50):
            self.pl_list.append(plist_Songs(self.rrf,self.music))
        

        # Getting Playlist
        if True:
            if True:
                self.Play_list = []
                for  i in cwd:
                    for folderName, _,_ in os.walk(i):
                        p = Path(folderName)
                        f = list(p.glob('*(list).txt'))
                        for j in f:
                            with open(j,"r") as df:
                                df = df.read().split("\n")
                                df = [j.name.replace("(list).txt",""),df[0],df[1:]]
                            self.Play_list.append(df)
            # print(Play_list)
            self.libb =[]
            # add a way to sample
            for j, i in enumerate(self.Play_list[:10]): # sample later
                self.libb.append(Ply_Songs(self.fr[j%5], *i, self.music, self.expand, sel, ))
    
    def expand(self, ty, pth ="", vie=""):
        if ty:
            self.masters.pack_forget()
            self.back.pack(anchor= W, pady= 5)
            self.on_list(pth,vie)
            self.rrf.pack(expand= True, fill= BOTH)
        elif not ty:
            if self.rev == 0:
                self.rev = 1
                self.focus()
                self.on_list(pth)
                self.expance()
                self.rrf.pack_forget()
            else:
                self.focus()
                self.on_list(pth)
                self.back.pack_forget()
                self.masters.pack(fill= X)
                self.rrf.pack_forget()
                self.lib(0)

    def expance(self):
        self.masters.pack_forget()
        self.back.pack(anchor= W, pady= 5)
        self.lib(trackk= self.Play_list)
        ...

    def on_list(self,path,vie=""):
        if path != "":
            tracks = []
            for i in path:
                i = Path(i)
                # for j in i:
                j1 = [j.lstrip() for j in i.name.replace(".mp3","").replace(".wav","").split("-")]
                if len(j1) == 1 or len(j1)>3:
                    j1 = ["UNKNOWN_ARTIST", "_".join(j1)]
                if len(j1) == 3:
                    j2 = j1[2] if not j1[2].startswith(" ") else j1[2][1:]
                    j1 = [j2, "_".join(j1[:2])]
                tracks.append([str(i),*j1])
            self.music.playlist[vie] = []
            for j,i in enumerate(tracks):
                self.pl_list[j].view("~".join(i[1:]), i[0], vie)
                self.music.playlist[vie].append(";'".join((i[0], "~".join(i[1:]))))
        else:
            for i in self.pl_list:
                i.view(path)

    def lib(self, k=1, trackk = ["",""]):
        if k:
            for i in trackk:
                self.tree.pack(fill=BOTH, expand=True)
                item_name= i[0]
                sub_items_path = i[2]
                self.tree.insert("", "end", text= item_name, values=(sub_items_path, *i[1:]))
        else:
            self.tree.pack_forget()
            self.tree.selection_clear()
            self.tree.delete(*self.tree.get_children())

    def play_song(self, event):
        item = self.tree.item(self.tree.selection())["values"]
        name = self.tree.item(self.tree.selection())["text"]
        self.expand(ty=1, pth= item, vie= name)
        self.lib(0)
        self.rev = 0

    def toggle_select(self, event):
        item = self.tree.identify_row(event.y)
        if item not in self.tree.selection():
            self.tree.selection_add(item)
        else:
            self.tree.selection_remove(item)
        # self.show_selection()
        self.selected = item



class Musicplayer(ttk.Frame):
    # Create playlist, add to playlist : -> + (create)
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, padding= 10, **kwargs)
        self.pack(expand=True, fill= BOTH)
        # Usage example
        self.yt_downloader = YouTubeDownloader()
        self.search_list = ""
        self.results = []
        self.no_net = False
        self.music = music_bar(self, master)
        try:
            #self.yt_downloader.s.run(self.yt_downloader.main1) # first connecting the app start session
            self.no_net = False
        except:
            self.no_net = True
        
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
            # More coming
            Categories(self.cont1, self.music, self)
            self.pl_cat = Playlist_Cat(self.cont1, self.music, self)
            # ttk.Label(self.cont1, text= "Most Played", font=("Helvetica", 13, "bold")).pack() # 
            # ttk.Label(self.cont1, text= "Albums", font=("Helvetica", 13, "bold")).pack()
            # ttk.Label(self.cont1, text= "Quick Pick", font=("Helvetica", 13, "bold")).pack()
            # ttk.Label(self.cont1, text= "Random Pick", font=("Helvetica", 13, "bold")).pack()
            ...

       
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

    def on_search_click(self): # make concurrent
        limit = 7
        bs = 5
        self.focus()
        if self.no_net == True:
            try:
                self.yt_downloader.s.run(self.yt_downloader.main1) # first connecting the app start session
                self.no_net = False
            except:
                Messagebox.show_error("No internet connnection", "networkerror")
        if self.no_net == False:
            if self.placeholder_color != "grey":
                print(self.search_entry.get())
                # self.load_bar.start()
                # self.load_bar.pack()
                # self.after(5000, self.searched)
                self.cont1.pack_forget()

                # searching
                result = self.yt_downloader.s.run(self.yt_downloader.main)[0]  # search result
                songl = "\n".join(result)
                print(songl)

                # # Store for safety
                # with open("search_list", "w") as f:
                #     f.write(songl)

                # # Load back
                # with open("search_list", "r") as f:
                #     result = f.read().split("\n")

                # result = result[:limit]
                # if limit < 10: bs = limit
                # tvb = threading.active_count()
                # self.yt_downloader.load(result, b=bs,t= tvb) # displaying

                # too = "\n".join("~".join(i) for i in self.yt_downloader.songlist)

                # with open("dependencies\song_list.txt", "wb") as f:
                #     f.write(too.encode())

                # with open("dependencies\song_list.txt", "rb") as f:
                #     self.search_list = f.read().decode()
                # self.search_list = [i.split("~") for i in self.search_list.split("\n")]
                
                # # intiating the widgets
                # self.cont1.pack_forget()
                # self.container.pack(fill= X) # scroll contaner
                # self.best_l.pack(anchor=W, padx=10, pady=10)
                # self.best_pick.view(f"{self.search_list[0][0].title()[:50]}~Song ● {self.search_list[0][2]} ● 2:45")
                # self.oth_l.pack(anchor=W, padx=10, pady= 10)
                # for i in range(len(self.search_list[1:]))[0:5]:
                #     # if i == 0: continue
                #     self.results[i].view(f"{self.search_list[i][0].title()[:50]}~Song ● {self.search_list[i][2]} ● 2:45")
                # print()#self.search_list[0][0] # song title, self.search_list[0][0] # song author

    def on_back_seach(self):
        self.focus()
        # intiating the widgets
        if self.search_list != []:
            self.search_list = []
            self.search_entry.delete(0,END)
            self.placeholder(0, 1)
            self.container.pack_forget() # scroll contaner
            self.cont1.pack(expand= True, fill= BOTH)
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
    sze = [5,3]
    scale= 200
    sze[0],sze[1] = sze[0]*scale,sze[1]*scale
    sze= tuple(sze)
    icon_path = r"imgs\Untitled design (2).png"
    app = ttk.Window(
        themename="superhero",
        title="TubePlayer",
        iconphoto= icon_path,
        size=sze,
        resizable=(False, False),
        )
    Musicplayer(app)
    app.mainloop()
