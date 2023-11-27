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


from tkinter import StringVar
import pygame.mixer as mixer
import pygame
import threading

class Music:
    status = ''
    def __init__(self):
        mixer.init()
        self.current_song = ''
        self.playlist = []

    # Play, Stop, Load and Pause & Resume functions
    def play_song(self, song_names):#, status: StringVar):
        # Add all the songs in the playlist to the queue
        for song_name in song_names:
            self.playlist.append(song_name)
            mixer.music.queue(song_name)

        # Play the first song in the playlist
        self.current_song = self.playlist.pop(0)
        mixer.music.load(self.current_song)
        mixer.music.play()
        self.status = "Song PLAYING"
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

        # Listen for the end of the song
        while self.status == "Song PLAYING":
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    if len(self.playlist) > 0:
                        # Load and play the next song in the playlist
                        self.current_song = self.playlist.pop(0)
                        mixer.music.load(self.current_song)
                        mixer.music.play()
                    else:
                        # Stop playing music if the playlist is empty
                        self.stop_song()

    def stop_song(self):
        mixer.music.stop()
        self.status = "Song STOPPED"

    def resume_pause_song(self):
        if self.status == "Song PAUSED":
            mixer.music.unpause()
            self.status = "Song RESUMED"
        elif self.status == "Song RESUMED" or self.status == "Song PLAYING":
            mixer.music.pause()
            self.status = "Song PAUSED"

    def play_song_thread(self, song_names):
        t = threading.Thread(target=self.play_song, args=(song_names,))
        t.start()
