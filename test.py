# # # import ttkbootstrap as ttk
# # # from tkinter import *
# # # from ttkbootstrap.constants import *
# # # from ttkbootstrap.icons import Emoji

# # # root = ttk.Window(themename="superhero")
# # # root.title("Search Bar")
# # # root.geometry('400x200')

# # # class Songs(ttk.Frame):
# # #     def __init__(self, master, nam, **kwargs) -> None:
# # #         super().__init__(master, padding= 10, **kwargs)
# # #         self.pack()
# # #         self.name = nam if len(nam) < 12 else nam[:12]+"\n"+nam[12:]
# # #         lab_img2 = ttk.Label(self, text= Emoji.get("MUSICAL NOTE"), bootstyle= (SECONDARY, INVERSE),
# # #                     font= ("Helvetica", 40), padding= 10)
# # #         lab_img2.pack(padx=10, pady= 0)

# # #         l1 = ttk.Label(self, text= self.name if len(self.name) < 20 else str(self.name[:20])+"...", bootstyle= PRIMARY, justify= CENTER)
# # #         l1.pack(side=BOTTOM)


# # # Songs(root, "poppppppppppppppppppppppppppp")

# # # root.mainloop()

# # # import glob
# # # import os

# # # def find_music_files(path, extensions):
# # #     found_files = []
# # #     for ext in extensions:
# # #         for file_path in glob.glob(f"{path}/*.{ext}"):
# # #             found_files.append(file_path)

# # #     return found_files

# # # music_extensions = ['mp3', 'wav']
# # # start_directory = os.path.expanduser("~")
# # # music_files = find_music_files(start_directory, music_extensions)

# # # print(music_files)

# # # for music_file in music_files:
# # #     # Perform operations with the music_file, e.g. add it to a playlist
# # #     pass

# # import tkinter as tk
# # from tkinter.filedialog import askdirectory
# # import os

# # import tkinter as tk
# # from PIL import Image
# # from io import BytesIO


# # def load_and_optimize_image(file_path):
# #     image = Image.open(file_path)
# #     optimized_image = image.resize((100, 100))  # Adjust the size as needed
# #     return optimized_image


# # music_player = tk.Tk()
# # music_player.title("My Music Player")
# # music_player.geometry("450x350")

# # directory = askdirectory()
# # os.chdir(directory)
# # song_list = os.listdir()

# # play_list = tk.Listbox(music_player, font="Helvetica 10 bold", bg='yellow', selectmode=tk.SINGLE)
# # for item in song_list:
# #     # print(item)
# #     play_list.insert(0, item)

# # play_list.pack(fill="both", expand="yes")

# # image_path = r"C:\Users\ajuga\OneDrive\Documents\Jupiter-python-try\learn\networking\musicplayer\peter (1).png"  # Replace with the path to your image file
# # optimized_image = load_and_optimize_image(image_path)

# # image_label = tk.Label(music_player)
# # image_label.pack(side="bottom", fill="both", expand="yes")
# # image_label.image = optimized_image


# # music_player.mainloop()

# # import os
# # from pathlib import Path
# # Songs_listt = []
# # cwd = [r"C:\Users\ajuga\Music", r"C:\Users\ajuga\OneDrive\Documents\Jupiter-python-try\learn\networking\musicplayer"]

# # for  i in cwd:
# #     for folderName, subfolders, filenames in os.walk(i):
# #         p = Path(folderName)
# #         f = list(i for i in p.glob('*.mp3') if not i.name.startswith("verse") \
# #                 and str(i).split(os.sep)[3] != 'AppData'\
# #                 and str(i).split(os.sep)[4] != 'games')
# #         if len(f) != 0:
# #             Songs_listt.append(f)
# #             # break
        
# # li = []
# # for i in Songs_listt:
# #     for j in i:
# #         j1 = j.name.replace(".mp3","").split("-")
# #         if len(j1) == 1 or len(j1)>3:
# #             j1 = ["_".join(j1), "UNKNOWN_ARTIST"]
# #         if len(j1) == 3:
# #             j1 = ["_".join(j1[:2]), j1[2]]
# #         # print(j)
# #         li.append([str(j),*j1])

# # print("\n".join(" ~ ".join(i) for i in li))

# # print("\n\n".join(",".join(i) for i in Songs_listt))


# if False:
#     # Importing all the necessary modules
#     from tkinter import *
#     from tkinter import filedialog
#     import pygame.mixer as mixer        # pip install pygame
#     import os

#     # Initializing the mixer
#     mixer.init()

#     # Creating the master GUI for python music player
#     root = Tk()
#     root.geometry('700x220')
#     root.title('PythonGeeks Music Player')
#     root.resizable(0, 0)


#     # Play, Stop, Load and Pause & Resume functions
#     def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
#         song_name.set(songs_list.get(ACTIVE))

#         mixer.music.load(songs_list.get(ACTIVE))
#         mixer.music.play()

#         status.set("Song PLAYING")


#     def stop_song(status: StringVar):
#         mixer.music.stop()
#         status.set("Song STOPPED")


#     def load(listbox):
#         os.chdir(filedialog.askdirectory(title='Open a songs directory'))

#         tracks = os.listdir()

#         for track in tracks:
#             listbox.insert(END, track)


#     def pause_song(status: StringVar):
#         mixer.music.pause()
#         status.set("Song PAUSED")


#     def resume_song(status: StringVar):
#         mixer.music.unpause()
#         status.set("Song RESUMED")

#     # All the frames
#     song_frame = LabelFrame(root, text='Current Song', bg='LightBlue', width=400, height=80)
#     song_frame.place(x=0, y=0)

#     button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120)
#     button_frame.place(y=80)

#     listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
#     listbox_frame.place(x=400, y=0, height=200, width=300)

#     # All StringVar variables
#     current_song = StringVar(root, value='<Not selected>')

#     song_status = StringVar(root, value='<Not Available>')


#     # Playlist ListBox
#     playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

#     scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
#     scroll_bar.pack(side=RIGHT, fill=BOTH)

#     playlist.config(yscrollcommand=scroll_bar.set)

#     scroll_bar.config(command=playlist.yview)

#     playlist.pack(fill=BOTH, padx=5, pady=5)

#     # SongFrame Labels
#     Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

#     song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
#     song_lbl.place(x=150, y=20)

#     # Buttons in the main screen
#     pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
#                         command=lambda: pause_song(song_status))
#     pause_btn.place(x=15, y=10)

#     stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
#                     command=lambda: stop_song(song_status))
#     stop_btn.place(x=105, y=10)

#     play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
#                     command=lambda: play_song(current_song, playlist, song_status))
#     play_btn.place(x=195, y=10)

#     resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,
#                         command=lambda: resume_song(song_status))
#     resume_btn.place(x=285, y=10)

#     load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35, command=lambda: load(playlist))
#     load_btn.place(x=10, y=55)


#     # Finalizing the GUI
#     root.update()
#     root.mainloop()

# # from tkinter import *
# # from tkinter import filedialog
# # import pygame.mixer as mixer
# # import os

# # class MusicPlayer:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.geometry('700x220')
# #         self.root.title('PythonGeeks Music Player')
# #         self.root.resizable(0, 0)

# #         # Initializing the mixer
# #         mixer.init()

# #         # Play, Stop, Load and Pause & Resume functions
# #         # self.play_song = self.play_song
# #         # self.stop_song = self.stop_song
# #         # self.load = self.load
# #         # self.pause_song = self.pause_song
# #         # self.resume_song = self.resume_song

# #         # Create and configure GUI elements
# #         # All the frames
# #         song_frame = LabelFrame(root, text='Current Song', bg='LightBlue', width=400, height=80)
# #         song_frame.place(x=0, y=0)

# #         button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120)
# #         button_frame.place(y=80)

# #         # listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
# #         # listbox_frame.place(x=400, y=0, height=200, width=300)

# #         # All StringVar variables
# #         current_song = StringVar(root, value='<Not selected>')

# #         song_status = StringVar(root, value='<Not Available>')


# #         # Playlist ListBox
# #         # playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

# #         # scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
# #         # scroll_bar.pack(side=RIGHT, fill=BOTH)

# #         # playlist.config(yscrollcommand=scroll_bar.set)

# #         # scroll_bar.config(command=playlist.yview)

# #         # playlist.pack(fill=BOTH, padx=5, pady=5)

# #         # SongFrame Labels
# #         Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

# #         song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
# #         song_lbl.place(x=150, y=20)

# #         # Buttons in the main screen
# #         # pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
# #         #                     command=lambda: self.pause_song(song_status))
# #         # pause_btn.place(x=15, y=10)

# #         stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
# #                         command=lambda: self.stop_song(song_status))
# #         stop_btn.place(x=105, y=10)

# #         play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
# #                         command=lambda: self.play_song(current_song, r"C:\Users\ajuga\Music\Alan-Walker\Alan Walker - Above The Sky.mp3", song_status))
# #         play_btn.place(x=195, y=10)

# #         # resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,
# #         #                     command=lambda: self.resume_song(song_status))
# #         # resume_btn.place(x=285, y=10)

# #         # load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35, command=lambda: load(playlist))
# #         # load_btn.place(x=10, y=55)


# #         # Finalizing the GUI
# #         self.root.update()
# #         self.root.mainloop()

# #     # Play, Stop, Load and Pause & Resume functions
# #     def play_song(self, song_name: StringVar, songs_list, status: StringVar):
# #         # song_name.set(songs_list.get(ACTIVE))

# #         mixer.music.load(songs_list)#songs_list.get(ACTIVE))
# #         mixer.music.play()

# #         status.set("Song PLAYING")


# #     def stop_song(self, status: StringVar):
# #         mixer.music.stop()
# #         status.set("Song STOPPED")


# #     def pause_song(self, status: StringVar):
# #         mixer.music.pause()
# #         status.set("Song PAUSED")


# #     def resume_song(self, status: StringVar):
# #         mixer.music.unpause()
# #         status.set("Song RESUMED")

# # # Create a MusicPlayer instance and run the GUI
# # if __name__ == "__main__":
# #     root = Tk()
# #     player = MusicPlayer(root)



# import pygame
# import tkinter as tk
# from tkinter import ttk

# def play():
#     pygame.mixer.music.play()

# def pause():
#     pygame.mixer.music.pause()

# def unpause():
#     pygame.mixer.music.unpause()

# def stop():
#     pygame.mixer.music.stop()

# def update_progress_bar():
#     current_pos = pygame.mixer.music.get_pos() / 1000
#     progress_var.set(current_pos)
#     progress_bar.after(1000, update_progress_bar)

# pygame.init()
# pygame.mixer.init()

# root = tk.Tk()
# root.title("Music Player")

# pygame.mixer.music.load(r"C:\Users\ajuga\Music\Benny_Blanco_feat_Halsey_feat_Khalid_Eastside.mp3")

# progress_var = tk.DoubleVar()
# progress_bar = ttk.Progressbar(root, length=300, mode="determinate", variable=progress_var)
# progress_bar.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# play_button = tk.Button(root, text="Play", command=play)
# play_button.grid(row=1, column=0, padx=5, pady=5)

# pause_button = tk.Button(root, text="Pause", command=pause)
# pause_button.grid(row=1, column=1, padx=5, pady=5)

# unpause_button = tk.Button(root, text="Unpause", command=unpause)
# unpause_button.grid(row=1, column=2, padx=5, pady=5)

# stop_button = tk.Button(root, text="Stop", command=stop)
# stop_button.grid(row=1, column=3, padx=5, pady=5)

# update_progress_bar()

# root.mainloop()
