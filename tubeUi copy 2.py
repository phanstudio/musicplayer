import os, threading, time
from tkinter import DoubleVar, BooleanVar, Menu
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Querybox, Messagebox
from tube_downloader import YouTubeDownloader
from pathlib import Path
from random import sample
from playeropy import Music
from PIL import Image
import multiprocessing as mp

# next part online part
class music_bar(Music):
    def __init__(self, root, mast):
        super().__init__()
        
        self.root = root
        self.status = ""
        self.song_index = 0
        # self.list_name = ""
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

        # self.mast.bind("<space>", lambda e: self.p_p_n(e,0)) # fix later
        # self.mast.bind("<Key-p>", lambda e: self.p_p_n(e,2))
        # self.mast.bind("<Key-n>", lambda e: self.p_p_n(e,1))

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
    
    def play_song(self, nam):
        self.play_btn.configure(text= Emoji.get('double vertical bar'))
        song_name = nam.split(";'")[1].split("~")
        self.l1.configure(text= song_name[1])
        self.l2.configure(text= song_name[0])
        self.song_index = self.playlist[self.list_name][self.song_index:].index(nam) + self.song_index
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
    def __init__(self, master, sel, btt, **kwargs) -> None:
        super().__init__(master, padding= 6, bootstyle= btt, **kwargs)
        # self.pack(expand= True, fill= X,padx=10, pady=5)
        self.name = ""#"\n".join(nam.split("~"))
        self.mess = False
        self.sel = sel
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

        self.db = ttk.Button(self.cont2, text= "Downlaod", command= self.download)
        self.db.pack(side= LEFT, expand= True, fill=X, padx= 5)
        self.progress_bar = ttk.Progressbar(self.cont2, orient=HORIZONTAL, length=200, mode='determinate')
        # ttk.Button(self.cont2, text= "Play", bootstyle= INFO).pack(side= LEFT, expand= True, fill=X, padx= 5)

    # def view(self, nam):
    #     self.name = nam
    #     if self.name != "":
    #         self.name = "\n".join(nam.split("~"))
    #         self.pack(expand= True, fill= X,padx=10, pady=5)
    #         self.l1.configure(text= self.name)
    #     else:
    #         self.pack_forget()
    def view(self, nam="", url=""):
        self.name = nam
        self.url = url
        if self.name != "":
            # self.url = url
            self.name = "\n".join(nam.split("~"))
            self.pack(expand= True, fill= X,padx=10, pady=5)
            self.l1.configure(text= self.name)
        else:
            self.pack_forget()
    
    def download(self):
        # add the download function here
        self.db.pack_forget()
        self.progress_bar.pack(side=BOTTOM, fill=X, padx=10,pady=5)
        self.sel.yt_downloader.download(self.url)
        self.sel.yt_downloader.prog = self.progress_bar
        self.sel.back_but.configure(state=DISABLED)
        self.sel.yt_downloader.back = self.sel.back_but
        self.mess = self.sel.yt_downloader.mess
        self.after(1000,lambda: self.err(5))
        ...

    def err(self, turns = 5): # fix
        if turns > 0:
            if len(self.mess) > 0:
                if self.mess[0] == True:
                    self.sel.yt_downloader.mess = []
                    self.mess = self.sel.yt_downloader.mess # incase
                    Messagebox.show_error("Bad Network", "Network Error")
            else:
                self.after(1000,lambda: self.err(turns-1)) 


class Songs(ttk.Frame):
    def __init__(self, master, nam="", sel="", **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.name = nam
        self.url = ""
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        self.sel = sel
        lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        self.l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 8), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝", command= self.kill)
        
        self.cont1.pack(fill= X)
        lab_img2.pack(side= LEFT, padx= 10)
        self.l1.pack(side=LEFT)
        self.b3.pack(side= RIGHT, padx= 10)
        self.cont2.pack(side= RIGHT, expand= True, fill=X, padx= 10)

        ttk.Button(self.cont2, text= "Downlaod", width=10, bootstyle= INFO, command= self.download).pack(side= RIGHT, fill=X, padx= 10)
        # ttk.Button(self.cont2, text= "Play", bootstyle= SECONDARY, width=10).pack(side= RIGHT, fill=X, padx= 10)
        self.progress_bar = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.pack(side=BOTTOM, fill=X, padx=10,pady=5)
    
    def view(self, nam="", url=""):
        self.name = nam
        self.url = url
        if self.name != "":
            # self.url = url
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
        self.sel.yt_downloader.download(self.url)
        self.sel.yt_downloader.prog = self.progress_bar
        self.sel.back_but.configure(state=DISABLED)
        self.sel.yt_downloader.back = self.sel.back_but
        self.mess = self.sel.yt_downloader.mess
        self.after(1000,lambda: self.err(5))
        ...

    def err(self, turns = 5): # fix
        if turns > 0:
            if len(self.mess) > 0:
                if self.mess[0] == True:
                    self.sel.yt_downloader.mess = []
                    self.mess = self.sel.yt_downloader.mess # incase
                    Messagebox.show_error("Bad Network", "Network Error")
            else:
                self.after(1000,lambda: self.err(turns-1)) 

    def kill(self):
        self.sel.yt_downloader.kill_thread()
        pass

class Tree_top_level(ttk.Toplevel):
    def __init__(self, music, pathn = [], li=[], sel= "", title="ttkbootstrap", iconphoto='', size=None, position=None, minsize=None, maxsize=None, resizable=None, transient=None, overrideredirect=False, windowtype=None, topmost=False, toolwindow=False, alpha=1, **kwargs):
        super().__init__(title, iconphoto, size, position, minsize, maxsize, resizable, transient, overrideredirect, windowtype, topmost, toolwindow, alpha, **kwargs)
        # self.top_level = ttk.Toplevel(self.music)
        self.attributes("-toolwindow", 1)  # Remove the window decorations
        self.resizable(0, 0)
        self.geometry("+%d+%d" % (music.mast.winfo_x(), music.mast.winfo_y()))
        self.config(padx=10, pady=10)
        self.wm_title("SelectPlaylst")  # Set the window title
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.close_top_level)
        self.li = li
        self.path_name = pathn
        self.create_top_level()
        self.sel = sel
        

    def create_top_level(self):
        self.tree = ttk.Treeview(self, show= "tree")
        self.tree.column("#0", width=200, stretch=ttk.NO)
        self.tree.bind("<Button-1>", self.toggle_select)

        self.tree.heading("#0", text="")
        self.tree.pack(fill=BOTH, expand=True)
        for i in self.li:
            self.tree.insert("", "end", text= i)

        ttk.Separator(self).pack(pady=10, fill= X)
        close_button = ttk.Button(self, text="Cancle", command=self.close_top_level)
        close_button.pack(side= RIGHT)
        submit_button = ttk.Button(self, text="Submit", command=self.submit)
        submit_button.pack(side= LEFT)

    def close_top_level(self):
        self.grab_release()
        self.destroy()
    
    def submit(self):
        item = self.tree.item(self.tree.selection())["text"]
        
        with open(f"./dependencies/custom_playlist/{item}(list).txt") as f:
            data = f.readlines()
        for i in self.path_name:
            data.append("\n"+i[1])
        with open(f"./dependencies/custom_playlist/{item}(list).txt", "w") as f:
            f.writelines(data)
        for i in self.sel.pl_cat.libb:
            # print(len(i.name.lower().strip()), len(item))
            if i.name.lower().strip() == item:
                if len(self.path_name) == 1:
                    i.pth.append(self.path_name[0][1])
                    Messagebox.show_info(f"({'-'.join(self.path_name[0][0]).title()}) added to {item.title()}")
                else:
                    i.pth = i.pth + [i[1] for i in self.path_name]
                    Messagebox.show_info(f"({len(self.path_name)} items) added to {item.title()}")
                
                break
        
        self.grab_release()
        self.destroy()

    def toggle_select(self, event):
        item = self.tree.identify_row(event.y)
        if item not in self.tree.selection():
            self.tree.selection_add(item)
        else:
            self.tree.selection_remove(item)
        # self.show_selection()
        self.selected = item


class lib_Songs(ttk.Frame):
    def __init__(self, master, nam="", path= "", music="", sel="", limt:int=16, **kwargs) -> None:
        super().__init__(master, padding= 0, **kwargs)
        self.pack(expand= True, fill= X,padx=0, pady=5, anchor= N)
        self.music = music
        self.path_name = [nam.split("~"), path]
        self.li_name = "track1"
        nam = [i if len(i) < limt else i[:limt]+".." for i in nam.split("~")]
        self.name = "\n".join(nam)
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        self.sel = sel
        # create_button = ttk.Button(self, text="Create Top Level", command=self.create_top_level)
        # create_button.pack()
        self.lab_img2 = ttk.Label(self.cont1, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
                    font= ("Helvetica", 15), padding= 10)
        
        self.lab_img2.bind("<Enter>", lambda e: self.hov(e, 0))
        self.lab_img2.bind("<Leave>", lambda e: self.hov(e, 1))
        self.lab_img2.bind("<Button-1>", self.play)
        
        self.l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 7), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝", command= self.menu_popup)

        self.popup_menu = Menu(self.cont1, tearoff=0)
        self.popup_menu.add_command(label="Add to Queue", command= self.add_to_queue)
        self.popup_menu.add_command(label="Add to Playlist", command= self.add_to_list)
        
        self.cont1.pack(fill= X)
        self.lab_img2.pack(side= LEFT)
        self.l1.pack(side=LEFT, padx= 2.5)
        self.b3.pack(side= RIGHT)
        self.cont2.pack(side= RIGHT)
        # ttk.Button(self.cont2, text= "⭐", bootstyle= (SECONDARY, LINK), command= lambda: self.focus()).pack(side= RIGHT)

    def hov(self,event,ty):
        if not ty:
            self.lab_img2.configure(text=" "+str(Emoji.get('black right-pointing triangle'))+" ")#"▶️")
        elif ty:
            self.lab_img2.configure(text= Emoji.get("MUSICAL NOTE"))
        pass

    def play(self, event):
        name = self.path_name[0]
        path = self.path_name[1]
        item = ";'".join((path,"~".join(name)))
        if self.music.list_name != self.li_name:
            self.music.list_name = self.li_name
            self.music.song_index = 0
        self.music.play_song(item)
        # add songs when limit reached random songs

    def menu_popup(self):
        self.focus()
        try:
            self.popup_menu.tk_popup(self.b3.winfo_rootx()-100, self.b3.winfo_rooty()+40, 0)
        finally:
            self.popup_menu.grab_release()

    def add_to_queue(self):
        item = ";'".join((self.path_name[1],"~".join(self.path_name[0])))
        if self.music.list_name != "":
            ss = self.music.playlist[self.music.list_name]
            ss1 = ss[:self.music.song_index+1] + [item]+ ss[self.music.song_index+1:]
            self.music.playlist[self.music.list_name] = ss1
        # Messagebox.show_info(f"({'-'.join(self.path_name[0]).title()}) added to Queue")

    def add_to_list(self):
        li =[]
        for folderName, _,_ in os.walk("./dependencies/custom_playlist"):
            p = Path(folderName)
            f = list(p.glob('*(list).txt'))
            for j in f:
                li.append(j.name.replace("(list).txt",""))

        # img_path = "imgs\peter (1).png"
        # img = ttk.PhotoImage(file=img_path).subsample(4,4)
        Tree_top_level(self.music, [self.path_name], li, self.sel)
        ...

    

class plist_Songs(ttk.Frame):
    def __init__(self, master, music="", limt:int=16, **kwargs) -> None:
        super().__init__(master, padding= 0, **kwargs)
        # self.pack(expand= True, fill= X, padx=0, pady=5, anchor= N)
        self.music = music
        self.view()
        self.cont1 = ttk.Frame(self)
        self.cont2 = ttk.Frame(self.cont1)
        self.lit_name = ''
        
        self.l1 = ttk.Label(self.cont1, text= self.name, font=("bold", 7), justify= LEFT)
        self.b3 = ttk.Button(self.cont1, bootstyle= LINK, text= "⁝") # change to delete
        
        self.cont1.pack(fill= X)
        # self.lab_img2.pack(side= LEFT)
        self.l1.pack(side=LEFT, padx= 2.5)
        self.b3.pack(side= RIGHT)
        self.cont2.pack(side= RIGHT)
        # ttk.Button(self.cont2, text= "⭐", bootstyle= (SECONDARY, LINK), command= lambda: self.focus()).pack(side= RIGHT)
        ttk.Button(self.cont2, text=" "+str(Emoji.get('black right-pointing triangle'))+" ", 
                   bootstyle= (SECONDARY, LINK), command= self.play).pack(side= RIGHT)

    def view(self, nam="", path="", vie=""):
        self.name = nam
        if self.name != "":
            self.path_name = [nam.split("~")]+[path]
            self.lit_name = vie
            self.name = "\n".join(nam.split("~"))
            self.pack(expand= True, fill= X, padx=10, pady=5)
            self.l1.configure(text= self.name)
        else:
            self.pack_forget()

    def play(self):
        name = self.path_name[0]
        path = self.path_name[1]
        item = ";'".join((path,"~".join(name)))
        if self.music.list_name != self.lit_name:
            self.music.list_name = self.lit_name
            self.music.song_index = 0
        self.music.play_song(item)

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
        self.pth = self.pth if self.pth != [""] else ""
        self.masters(ty=1, pth= self.pth, vie= self.name)



class Categories(ttk.Frame):
    def __init__(self, master, music, sel, fram, **kwargs) -> None:
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
        self.add_var = BooleanVar()
        self.selections = []
        self.states = 0
        self.fram = fram

        self.tree = ttk.Treeview(self.fram, selectmode= "none", height= 13, columns=("Artist"))
        self.tree.heading("#0", text="Song")
        self.tree.heading("Artist", text="Artist")
        self.tree.selection_clear()
        self.tree.bind("<Double-1>", self.play_song)
        self.tree.bind("<Button-1>", self.toggle_select)
        # self.tree.bind("<Button-3>", self.add_to_list)

        self.detached_items = set(self.tree.get_children())
        
        self.selm = ttk.Frame(self.fram)
        self.back = ttk.Button(self.selm, text= "Back", bootstyle= SECONDARY, command= lambda: self.expand(0))
        self.back.pack(anchor= W, pady= 5, side=LEFT)
        self.add = ttk.Checkbutton(self.selm, text= "+ Add to Playlist", bootstyle= SECONDARY,
                                    command= self.addd, variable= self.add_var, compound= RIGHT)
        self.add.pack(anchor= W, pady= 5, side=RIGHT)
        self.addto = ttk.Button(self.selm, text= "Add", bootstyle= INFO, command= self.add_to_list)
        self.toend = ttk.Button(self.selm, text= "X", bootstyle= LINK, command= self.deselect_all)
        

        self.cont1 = ttk.Frame(self.mast)
        self.cont1.pack(fill= X)
        ttk.Label(self.cont1, text= "Libary", font=("Helvetica", 13, "bold")).pack(side= LEFT)
        ttk.Button(self.cont1, text= "More", bootstyle= SECONDARY, command= lambda: self.expand(1)).pack(side= RIGHT)
        ttk.Button(self.cont1, text= "↻", bootstyle= (LINK), command= self.refresh).pack(side= RIGHT)
        self.b3 = ttk.Button(self.cont1, text= "+", bootstyle= (LINK), command= self.menu_popup)
        self.b3.pack(side= RIGHT)

        self.popup_menu = Menu(self.cont1, tearoff=0)
        self.popup_menu.add_command(label="Create From Existing", command= self.add_to)
        self.popup_menu.add_command(label="Create New", command= self.add_new)

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
                self.libb.append(lib_Songs(self.fr[j%3], "~".join(i[1:]), i[0], self.music, self.sel))
                self.music.playlist["track1"].append(";'".join((i[0], "~".join(i[1:]))))

    def deselect_all(self):
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def play_song(self, event):
        item = self.tree.item(self.tree.selection())["values"]
        nam = item[1]
        path = item[2]
        auth = item[0]
        name = (auth,nam)
        item = ";'".join((path,"~".join(name)))
        if self.music.list_name != "track2":
            self.music.list_name = "track2"
            self.music.song_index = 0
        self.music.play_song(item)

    def toggle_select(self, event):
        if self.states == False:
            for i in self.tree.selection():
                self.tree.selection_remove(i)
        item = self.tree.identify_row(event.y)
        if item not in self.tree.selection():
            self.tree.selection_add(item)
        else:
            self.tree.selection_remove(item)
        self.selected = item
        if len(self.tree.selection()) != 0 and self.states == True:
            self.addto.pack(anchor= W, pady= 5, padx= 5, side=RIGHT)
            self.toend.pack(anchor= W, pady= 5, side=RIGHT)
        else:
            self.addto.pack_forget()
            self.toend.pack_forget()
        

    def undo_search(self):
        if "track2" in self.music.playlist.keys(): #ineffecient
            for child in self.detached_items:
                self.tree.detach(child)
            dt = list(self.detached_items)
            dt.sort()
            for child in dt:
                self.tree.reattach(child, '', END)
            self.music.playlist["track2"].clear()
            for i in self.tree.get_children():
                item = self.tree.item(i)['values']
                self.music.playlist["track2"].append(";'".join((item[2], "~".join(map(str,item[:2])))))
            self.music.song_index = 0

    def expand(self, ty):
        if ty:
            self.view = "li"
            self.masters.pack_forget()
            self.selm.pack(fill= X)
            # self.back.pack(anchor= W, pady= 5)
            self.lib(trackk= self.songtrack)
            self.sel.search_state = 0
        elif not ty:
            self.sel.on_cancle_search()
            self.view = "ui"
            self.lib(0)
            self.selm.pack_forget()
            self.masters.pack(fill= X)
            self.sel.back_but.configure(state=ACTIVE)
            self.sel.search_state = 0            
    
    def lib(self, k=1, trackk = ["",""]):
        if k:
            self.music.playlist["track2"] = []
            for i in trackk:
                self.tree.pack(fill=BOTH, expand=True)
                item_path = i[0]
                if os.path.isfile(item_path):
                    self.tree.insert("", "end", text= i[2], values=(*i[1:], item_path))
                    self.music.playlist["track2"].append(";'".join((i[0], "~".join(i[1:]))))
            self.detached_items = set(self.tree.get_children()) # check later
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
            # print("\n".join(i.split(";")[0] for i in self.music.playlist["track1"])) # errror found
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
    
    def add_new(self): # add an input
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
            # print("\n".join(i.split(";")[0] for i in self.music.playlist["track1"])) # errror found
            with open(f"dependencies\\custom_playlist\\{name}", "wb") as f:
                f.write(
                ("imgs\peter (1).png").encode()
                )
            li = [name.replace("(list).txt", ""), "imgs\peter (1).png"]
            lenn = len(self.sel.pl_cat.libb)
            self.sel.pl_cat.Play_list.append(li)
            if lenn < 10:
                self.sel.pl_cat.libb.append(Ply_Songs(self.sel.pl_cat.fr[(lenn)%5], img_path= li[1], nam= li[0]
                                                    ,music = self.sel.pl_cat.music, mast = self.sel.pl_cat.expand,sel= self.sel))
        
        ...

    def menu_popup(self):
        self.focus()
        try:
            self.popup_menu.tk_popup(self.b3.winfo_rootx()-100, self.b3.winfo_rooty()+40, 0)
        finally:
            self.popup_menu.grab_release()

    def add_to_list(self, event=0):
        li =[]
        for folderName, _,_ in os.walk("./dependencies/custom_playlist"):
            p = Path(folderName)
            f = list(p.glob('*(list).txt'))
            for j in f:
                li.append(j.name.replace("(list).txt",""))
        ly = []
        for i in self.tree.selection():
            item = self.tree.item(i)["values"]
            nam = item[1]
            path = item[2]
            auth = item[0]
            ly.append([[auth,nam],path])
        Tree_top_level(self.music, ly, li, self.sel)
        for i in self.tree.selection():
            self.tree.selection_remove(i)
        # print(self.sel.pl_cat.libb[0].name)
        ...

    def addd(self):
        self.addto.pack_forget()
        self.toend.pack_forget()
        self.states = self.add_var.get()
        ...


class Playlist_Cat(ttk.Frame):
    # Add no playlist
    def __init__(self, master, music, sel, fram, **kwargs) -> None:
        super().__init__(master, padding= 6, **kwargs)
        self.pack(expand= True, fill= X,padx=80, pady=5)
        self.masters = master
        self.rev = 1
        self.mast = ttk.Frame(self, bootstyle= SECONDARY)
        cwd_music = os.path.expanduser("~")+"\Music"
        cwd = [cwd_music, r"./dependencies/custom_playlist"] # fix
        self.mast.pack(fill= X)
        self.music = music
        self.sel = sel
        self.fram = fram
        
        self.selm = ttk.Frame(fram)
        self.back = ttk.Button(self.selm, text= "Back", bootstyle= SECONDARY, command= lambda: self.expand(0))
        self.plus = ttk.Button(self.selm, text= "+", bootstyle= LINK, width=5, command= self.mov_add)
        self.plus.pack(side= RIGHT)
        self.back.pack(anchor= W, pady= 5, side= LEFT)
        self.tree = ttk.Treeview(fram, selectmode= BROWSE, height= 13)
        self.tree.heading("#0", text="Playlist", anchor= "w")
        self.tree.selection_clear()
        self.tree.bind("<Double-1>", self.play_song)
        self.tree.bind("<Button-1>", self.toggle_select)
        self.tree.bind("<Button-3>", self.tselect)
        self.detached_items = set(self.tree.get_children())
 
        self.cont1 = ttk.Frame(self.mast)
        self.cont1.pack(fill= X)
        ttk.Label(self.cont1, text= "Playlist", font=("Helvetica", 13, "bold")).pack(side= LEFT)
        ttk.Button(self.cont1, text= "More", bootstyle= SECONDARY, command= self.expance).pack(side= RIGHT) # to mange more playlist
        ttk.Button(self.cont1, text= "🗑️", bootstyle= OUTLINE, width=5, command= self.mov_del).pack(side= RIGHT, padx=5)
        self.fr = [ttk.Frame(self.mast) for _ in range(5)]
        for i in range(5):
            self.fr[i].pack(side= LEFT, expand= True, fill=BOTH)

        self.rrf = ScrolledFrame(sel, height= 400)
        self.pl_list = []
        for _ in range(50):
            self.pl_list.append(plist_Songs(self.rrf, self.music))
        

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
            self.libb =[]
            # add a way to sample
            for j, i in enumerate(self.Play_list[:10]): # sample later
                self.libb.append(Ply_Songs(self.fr[j%5], *i, self.music, self.expand, sel, ))
    
    def expand(self, ty, pth ="", vie=""):
        if ty:
            self.masters.pack_forget()
            self.selm.pack(fill=X)
            self.on_list(pth,vie)
            self.rrf.pack(expand= True, fill= BOTH)
            # self.sel.search_state = 1
        elif not ty:
            if self.rev == 0:
                self.rev = 1
                self.focus()
                self.on_list(pth)
                self.expance()
                self.rrf.pack_forget()
                # self.sel.search_state = 0
            else:
                self.sel.on_cancle_search()
                self.focus()
                self.on_list(pth)
                self.selm.pack_forget()
                self.masters.pack(fill= X)
                self.rrf.pack_forget()
                self.lib(0)
                self.sel.search_state = 0

    def expance(self):
        self.masters.pack_forget()
        self.selm.pack(fill=X)
        self.lib(trackk= self.Play_list)
        self.sel.search_state = 1
        ...

    def on_list(self,path,vie=""):
        if path != "":
            self.plus.pack(side= RIGHT)
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
            self.plus.pack_forget()
            for i in self.pl_list:
                i.view(path)

    def lib(self, k=1, trackk = ["",""]):
        if k:
            for i in trackk:
                self.tree.pack(fill=BOTH, expand=True)
                item_name= i[0]
                sub_items_path = i[2] if len(i) == 3 else ""
                i.append([]) if len(i) == 2 else i
                self.tree.insert("", "end", text= item_name, values=(i[1],*i[2]))
            self.detached_items = set(self.tree.get_children()) 
        else:
            self.tree.pack_forget()
            self.tree.selection_clear()
            self.tree.delete(*self.tree.get_children())

    def play_song(self, event):
        item = self.tree.item(self.tree.selection())["values"]
        name = self.tree.item(self.tree.selection())["text"]
        # item[0] image file
        pth = [*item[1:]] if item[0] != "" else ""
        self.expand(ty=1, pth= pth, vie= name)
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

    def tselect(self, event):
        item = self.tree.identify_row(event.y)
        self.popup_menu = Menu(self.cont1, tearoff=0)
        self.popup_menu.add_command(label="Delete Playlist", command= self.del_to)
        self.focus()
        for i in self.tree.selection():
            self.tree.selection_remove(i)
        if item not in self.tree.selection():
            self.tree.selection_add(item)
            self.selected = item
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def del_to(self):
        name = self.tree.item(self.tree.selection())['text']
        self.tree.detach(self.tree.selection())
        os.remove(f"./dependencies/custom_playlist/{name}(list).txt")
        self.Play_list.clear()
        for folderName, _,_ in os.walk(r"./dependencies/custom_playlist"):
            p = Path(folderName)
            f = list(p.glob('*(list).txt'))
            for j in f:
                with open(j,"r") as df:
                    df = df.read().split("\n")
                    df = [j.name.replace("(list).txt",""),df[0],df[1:]]
                self.Play_list.append(df)
        for i in self.libb:
            i.destroy()
        self.libb.clear()
        for j, i in enumerate(self.Play_list[:10]): # sample later
            self.libb.append(Ply_Songs(self.fr[j%5], *i, self.music, self.expand, self.sel, ))
        # self.libb.append(Ply_Songs(self.fr[j%5], *i, self.music, self.expand, self.sel))
        
        
        ...

    def mov_del(self):
        self.expance()
        Messagebox.show_info("RightClick to delete")
        ...

    def mov_add(self):
        self.expand(0)
        self.expand(0)
        self.sel.catie.expand(1)
        # add show hint option
        Messagebox.show_info("Click on add to playlist to add to playlist")
        ...

    def undo_search(self):
        for child in self.detached_items:
            self.tree.detach(child)
        dt = list(self.detached_items)
        dt.sort()
        # print()
        for child in dt:
            # print(child)
            self.tree.reattach(child, '', END)


class Musicplayer(ttk.Frame):
    # Create playlist, add to playlist : -> + (create)
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, padding= 10, **kwargs)
        self.pack(expand=True, fill= BOTH)
        # Usage example
        self.yt_downloader = YouTubeDownloader()
        self.search_list = []
        self.results = []
        self.music = music_bar(self, master)
        self.page = 1
        self.offline = False
        self.offline_var = BooleanVar()
        self.search_state = 0
        
        self.holder = "Search songs,albums,artists..."
        self.placeholder_color = "grey"
        self.default_fg_color = "white"
        
        song = "i love her eyes".title()
        author_name = "billie ellise".title()
        my_style = ttk.Style()
        my_style.configure('Link.TButton', font=("Helvetica", 15))
        

        if True: # Search
            searchf = ttk.Frame(self)
            searchf.pack(fill= X, padx= 80)
            self.check = ttk.Checkbutton(searchf, text="Offline", bootstyle="info", command=self.off_on, variable= self.offline_var)
            self.check.pack(side= RIGHT, padx=5)
            search_frame = ttk.Frame(searchf)
            search_frame.pack(pady=20, fill= X)#, padx= 80)
            self.back_but = ttk.Button(search_frame,text= "<", bootstyle= SECONDARY, command= self.on_back_seach)
            self.back_but.pack(side= LEFT)

            self.search_entry = ttk.Entry(search_frame)
            self.search_entry.pack(side=LEFT, padx=5, fill= X, expand=True)
            self.search_entry.configure(foreground= self.placeholder_color)
            self.search_entry.insert(0, self.holder)
            self.canc_sech = ttk.Button(search_frame,text= "✕", bootstyle= SECONDARY, command= self.on_cancle_search) # add offline search

            search_button = ttk.Button(search_frame, text="Search", bootstyle="info", command=self.search)
            search_button.pack(side=LEFT, padx= 5)
            self.search_entry.bind("<FocusIn>", lambda e: self.placeholder(e, 0))
            self.search_entry.bind("<FocusOut>", lambda e: self.placeholder(e, 1))

            
            
            self.load_bar = ttk.Progressbar(self, mode= INDETERMINATE, length= 400)
            self.container = ScrolledFrame(self, height= 430, autohide= True)
            self.lodd = ttk.LabelFrame(self.container, text= "Searched")
            self.lodd.pack(fill= X, padx= 80)
            
            # Search section
            s_frame = ttk.Frame(self.lodd)
            s_frame.pack(fill= X)
            self.best_l = ttk.Label(s_frame, text= "Best Result", font=("Helvetica", 13, "bold"))
            ttk.Button(s_frame, text= "NextPage", command= lambda: self.pp(1)).pack(side= RIGHT, padx= 10)
            ttk.Button(s_frame, text= "PrevPage", command= lambda: self.pp(-1)).pack(side= RIGHT, padx= 5)
            self.best_pick = Def_Songs(self.lodd, self, SECONDARY)
            self.oth_l = ttk.Label(self.lodd, text= "Other Songs", font=("Helvetica", 13, "bold"))
            for _ in range(5):
                self.results.append(Songs(self.lodd, "", self))
            self.s1_frame = ttk.Frame(self.lodd)
            ttk.Button(self.s1_frame, text= "NextPage", command= lambda: self.pp(1)).pack(side= RIGHT, padx= 10)
            ttk.Button(self.s1_frame, text= "PrevPage", command= lambda: self.pp(-1)).pack(side= RIGHT, padx= 5)

            # self.create_songs_grid()

        if True: # home page
            self.fram = ttk.Frame(self)#, autohide= True)
            self.fram.pack(expand= True, fill= BOTH)
            self.cont1 = ScrolledFrame(self.fram, height= 400)#, autohide= True)
            self.cont1.pack(expand= True, fill= BOTH)
            

            # ttk.Label(self.cont1, text= "Favourite", font=("Helvetica", 13, "bold")).pack() # square
            # ttk.Label(self.cont1, text= "Libary", font=("Helvetica", 13, "bold")).pack()
            # More coming
            self.catie = Categories(self.cont1, self.music, self, self.fram)
            self.pl_cat = Playlist_Cat(self.cont1, self.music, self, self.fram)
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
                            # print(wig1.winfo_name())
                            pass
                # print()
                # print(wig.winfo_name())
        # play_btn.configure(text= Emoji.get('double vertical bar'))

    def off_search(self, sel):
        sel.undo_search() # error here
        try:
            self.fram.pack_info()
        except:
            self.fram.pack(expand= True, fill= BOTH)
        query = self.search_entry.get()
        # print(sel.rev)
        for child in sel.tree.get_children():
            # print(child)
            
            item_values = sel.tree.item(child)['values'] if self.search_state == 0 else sel.tree.item(child)['text']
            if query.lower() not in str(item_values).lower():
                sel.tree.detach(child)
        # print(sel.tree.get_children())
        if self.search_state == 0:
            sel.expand(1)
            self.music.playlist["track2"].clear()
            for i in sel.tree.get_children():
                item = sel.tree.item(i)['values']
                self.music.playlist["track2"].append(";'".join((item[2],"~".join(map(str,item[:2])))))
            self.music.song_index = 0

    def search(self):
        # print(self.search_entry.get() == 'Search songs,albums,artists...')
        if self.search_entry.get() != 'Search songs,albums,artists...':
            if self.offline == False:
                self.fram.pack_forget()
                p1 = threading.Thread(target= self.on_search_click)
                p1.start()
            else:
                self.back_but.configure(state=DISABLED)
                if self.search_state == 0:
                    self.off_search(self.catie)
                    # scroll contaner
                    try:
                        self.container.pack_info()
                        self.container.pack_forget() 
                        # self.cont1.pack(expand= True, fill= BOTH)
                    except:
                        pass
                    for i in range(len(self.search_list))[:5]:
                        self.results[i].view("")
                elif self.search_state == 1:
                    self.off_search(self.pl_cat)
                pass
        # p1.join()

    def on_search_click(self): # make concurrent
        if True:#self.placeholder_color != "grey":
            self.load_bar.start()
            self.load_bar.pack()
            # self.after(5000, self.searched)

            # searching
            self.yt_downloader.search(self.search_entry.get(),search_lenght= 25)
            
            
            # Store for safety
            enc = "\n~\n".join(["\n".join(f"{j}~{i}" for j, i in itn.items()) for itn in self.yt_downloader.songlist])
            self.searched()
            with open("dependencies\search_list.txt", "wb") as f:
                f.write(enc.encode())

            # Load back
            with open("dependencies\search_list.txt", "rb") as f:
                result = f.read().decode()
            if result != "":
                dec = [{j.split("~")[0]:j.split("~")[1] for j in i.split("\n")} for i in result.split("\n~\n")]
                t = [f"{i['title'].split('-')[0]}~{'-'.join(i['title'].split('-')[1:])}" if len(i['title'].split('-')) > 1 else f"Unknown Artist ~ {i['title']}" for i in dec]

                self.search_list = []
                for l,i in enumerate(dec):
                    self.search_list.append({k:t[l] if k == "title" else v for k,v in i.items()})
                search_list, self.search_list = self.search_list[0], self.search_list[1:]
            
                # intiating the widgets
                # self.cont1.pack_forget()
                self.container.pack(fill= X) # scroll contaner
                self.best_l.pack(anchor=W, padx=10, pady=10)
                self.best_pick.view(f"{search_list['title'].title().split('~')[0][:50]}~Song ● {search_list['title'].split('~')[1]} ● {search_list['length']}", search_list['url'])
                self.oth_l.pack(anchor=W, padx=10, pady= 10)
                for i in range(len(self.search_list))[0:5]:
                    song = self.search_list[i]['title'].title().split('~')
                    self.results[i].view(f"{song[0][:50]}~Song ● {song[1][:60] + '...' if len(song[1]) >= 60 else song[1]} ● {self.search_list[i]['length']}", self.search_list[i]['url'])
                self.s1_frame.pack(fill= X, pady= 10, padx= 30)
            else:
                # Messagebox.show_error("No internet connnection", "Networkerror") # eror handeling
                self.after(1000, self.err)


    def on_back_seach(self):
        self.focus()
        # intiating the widgets
        if self.search_list != []:
            self.search_list = []
            self.search_entry.delete(0,END)
            self.placeholder(0, 1)
            self.container.pack_forget() # scroll contaner
            # self.cont1.pack(expand= True, fill= BOTH)
            # self.best_l.pack_forget()
            # self.oth_l.pack_forget()
            for i in range(len(self.search_list))[:5]:
                self.results[i].view("")
            self.fram.pack(expand= True, fill= BOTH)

    def on_cancle_search(self):
        self.search_entry.focus()
        self.search_entry.delete(0, END)
        self.focus()
        self.canc_sech.pack_forget()
        if self.search_state == 0:
            self.catie.undo_search() # error here
        elif self.search_state == 1:
            self.pl_cat.undo_search()
        ...


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
    
    def pp(self, pg= 1):
        self.focus()
        self.page += pg
        if self.page > (len(self.search_list)//5)+1:
            self.page = (len(self.search_list)//5)+1
        elif self.page < 1:
            self.page = 1
        # print(self.page)
        
        for i in range(len(self.search_list))[5 * (self.page-1): 5 * self.page]:
            # print(5 ** (self.page-1), self.page)
            song = self.search_list[i]['title'].title().split('~')
            self.results[i%5].view(f"{song[0][:50]}~Song ● {song[1][:60] + '...' if len(song[1]) >= 60 else song[1]} ● {self.search_list[i]['length']}", self.search_list[i]['url'])
        if (len(self.search_list)//5)+1 == self.page:
            if len(self.search_list)%5 != 0:
                for i in range(5- (5 - (len(self.search_list)%5)),5):
                    self.results[i].view("")
        self.s1_frame.pack_forget()
        self.s1_frame.pack(fill= X, pady= 10, padx= 30)

    def off_on(self):
        if self.offline:
            if self.search_state == 0:
                try:
                    self.catie.expand(0)
                    self.pl_cat.expand(0)
                except:
                    pass
                pass
            else:
                self.pl_cat.undo_search()
                self.back_but.configure(state=ACTIVE)
        self.offline = self.offline_var.get()

    def err(self):
        Messagebox.show_error("No internet connnection", "Networkerror") # eror handeling
        self.search_list = ["",""]
        self.on_back_seach()
        self.search_list = []


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
