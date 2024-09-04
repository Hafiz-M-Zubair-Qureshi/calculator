import os
import tkinter as tk
from tkinter import filedialog
from tkinter import Listbox, messagebox
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x500")

        # Initialize Pygame mixer
        mixer.init()

        # Add title
        self.title_label = tk.Label(root, text="Music Player", font=("Arial", 15, "bold"))
        self.title_label.pack(pady=10)

        # Playlist Listbox
        self.playlist = Listbox(root, selectmode=tk.SINGLE, bg="lightgrey", fg="black", font=("Arial", 12), height=12, width=40)
        self.playlist.pack(padx=20, pady=10)

        # Add Buttons
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.play_button = tk.Button(self.buttons_frame, text="Play", command=self.play_song)
        self.play_button.grid(row=0, column=0, padx=10)

        self.pause_button = tk.Button(self.buttons_frame, text="Pause", command=self.pause_song)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.stop_button = tk.Button(self.buttons_frame, text="Stop", command=self.stop_song)
        self.stop_button.grid(row=0, column=2, padx=10)

        self.resume_button = tk.Button(self.buttons_frame, text="Resume", command=self.resume_song)
        self.resume_button.grid(row=0, column=3, padx=10)

        self.add_button = tk.Button(self.buttons_frame, text="Add Songs", command=self.add_songs)
        self.add_button.grid(row=1, column=0, columnspan=4, pady=10)

        # Volume Control
        self.volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(50)  # Set default volume
        mixer.music.set_volume(0.5)
        self.volume_scale.pack(pady=20)

        # Initialize variables
        self.current_song = None
        self.paused = False

    def add_songs(self):
        # Open file dialog to select song(s)
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3")])
        for file in files:
            self.playlist.insert(tk.END, file)

    def play_song(self):
        if self.playlist.curselection():
            self.stop_song()  # Stop current song (if any) before playing new song
            self.current_song = self.playlist.get(tk.ACTIVE)
            mixer.music.load(self.current_song)
            mixer.music.play()
            self.paused = False
        else:
            messagebox.showwarning("No selection", "Please select a song to play.")

    def stop_song(self):
        mixer.music.stop()

    def pause_song(self):
        if not self.paused:
            mixer.music.pause()
            self.paused = True

    def resume_song(self):
        if self.paused:
            mixer.music.unpause()
            self.paused = False

    def set_volume(self, val):
        volume = float(val) / 100
        mixer.music.set_volume(volume)

# Create the main window
root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
