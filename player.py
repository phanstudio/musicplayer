from tkinter import StringVar
import pygame.mixer as mixer


class Music:
    song_status = ''
    def __init__(self):
        mixer.init()
        current_song = ''

    # Play, Stop, Load and Pause & Resume functions
    def play_song(self, song_name, songs_list):#, status: StringVar):

        mixer.music.load(songs_list)
        mixer.music.play()
        self.status = "Song PLAYING"


    def stop_song(self): # Closing # after
        mixer.music.stop()
        self.status.set("Song STOPPED")

    def resume_pause_song(self):
        if self.status == "Song PAUSED":
            mixer.music.unpause()
            self.status = "Song RESUMED"
        elif self.status == "Song RESUMED" or self.status == "Song PLAYING":
            mixer.music.pause()
            self.status = "Song PAUSED"
