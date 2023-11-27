from tkinter import StringVar
import pygame.mixer as mixer
import pygame
import os
from mutagen.mp3 import MP3

class Music:
    song_status = 'Next'
    MUSIC_END = pygame.USEREVENT+1
    def __init__(self):
        # Initializing the mixer
        pygame.init()
        mixer.init()
        self.playlist = {}
        self.list_name = ''
        self.pos = 0
        self.update = False
        self.songlength = 0
        self.aft_can = 0
        # All StringVar variables
        current_song = ''

    # Play, Stop, Load and Pause & Resume functions
    def play_song(self):
        self.status = "Song PLAYING"
        song_path = self.playlist[self.list_name][self.song_index].split(";'")[0]
        try:
            mixer.music.load(song_path)
            mixer.music.play()
            self.set_timescale(song_path)
            self.pos = 0
            if self.aft_can != 0:
                self.progress_bar.after_cancel(self.aft_can)
                self.aft_can = 0
            self.update_progress_bar()
            mixer.music.set_endevent(self.MUSIC_END)
            self.check_event()
        except:
            if self.song_status == "Next":
                self.next_song()
            else:
                self.previous_song()
        
    def next_song(self):
        self.root.focus()
        self.song_status = "Next"
        if self.aft_can != 0:
            self.progress_bar.after_cancel(self.aft_can)
            self.aft_can = 0
            
        if self.song_index < len(self.playlist[self.list_name]) - 1:
            self.song_index = self.song_index + 1
        else: # repeat play list
            self.song_index = 0
        next_song_path = self.playlist[self.list_name][self.song_index]
        self.play_song(next_song_path)
    
    def previous_song(self):
        self.root.focus()
        if self.pos > 2:
            self.pos = 0
            mixer.music.set_pos(self.pos)
            self.progress_var.set(self.pos)
        else:
            self.song_status = "Prev"
            if self.song_index > 0:
                self.song_index = self.song_index - 1
            else: # repeat play list
                self.song_index = len(self.playlist[self.list_name]) - 1
            next_song_path = self.playlist[self.list_name][self.song_index]
            self.play_song(next_song_path)

    def stop_song(self):
        mixer.music.stop()
        self.status.set("Song STOPPED")

    def resume_pause_song(self):
        if self.status == "Song PAUSED":
            self.update = False
            mixer.music.unpause()
            self.status = "Song RESUMED"
        elif self.status == "Song RESUMED" or self.status == "Song PLAYING":
            self.update = True
            mixer.music.pause()
            self.status = "Song PAUSED"

    def getsonglen(self, song_path):
        s = mixer.Sound(song_path)
        songlength = s.get_length()
        return songlength

    def set_timescale(self, song_path):
        self.songlength = self.getsonglen(song_path)
        self.progress_bar.config(to=self.songlength)

    def update_progress_bar(self):
        if self.update == False:
            # if self.status ==
            self.pos += 1
            current_pos = self.pos
            self.progress_var.set(current_pos)
            self.updat(self.pos)
        self.aft_can = self.progress_bar.after(1000, self.update_progress_bar)

    def fast_forward(self):
        current_pos = self.pos
        self.pos = current_pos + 5
        mixer.music.set_pos(self.pos)
        self.progress_var.set(self.pos)
        self.updat(self.pos)
    
    def move_song(self, _= None):
        self.pos = self.progress_var.get()
        mixer.music.set_pos(self.pos)
        self.updat(self.pos)
    
    def change_volume(self, _= None):
        mixer.music.set_volume((self.volume_var.get())/10)
        self.fig.configure(text= f"{round(self.volume_var.get()*10)}")

    def renue(self):
        self.update = False

    def rewind_back(self):
        current_pos = self.pos
        new_pos = current_pos - 5#self.decr
        if new_pos <= 0:
            self.pos = 0
        else:
            self.pos = new_pos
        mixer.music.set_pos(self.pos)
        self.progress_var.set(self.pos)
        self.updat(self.pos)
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type == self.MUSIC_END:
                self.next_song() # Replace with your desired function
            # else:
        self.root.after(100, self.check_event)

    def updat(self, value):
        evall = self.songlength - value
        val = str(round(value//60)).rjust(2,"0")+ ":" + str(round(value%60)).rjust(2,"0")
        self.elaspe.configure(text=val)
        val1 = str(round(evall//60)).rjust(2,"0")+ ":" + str(round(evall%60)).rjust(2,"0")
        self.remain.configure(text=val1)
        ...
