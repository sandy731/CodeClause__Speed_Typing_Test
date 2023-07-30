import tkinter as tk
import time
import threading
import random


class TypeSpeed:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600")

        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("TimeNewRoman", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=30, font=("TimeNewRoman", 22))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text="Speed:  \n0.00 CPS\n0.00  CPM\n0.00 WPS\n0.00 WPM",
                                    font=("TimeNewRoman", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_btn = tk.Button(self.frame, text="Reset", command=self.reset, font=("TimeNew Roman", 24))
        self.reset_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.runing = False

        self.root.mainloop()

    def start(self, event):
        if not self.runing:
            if not event.keycode in [16, 17, 18]:
                self.runing = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.runing = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.runing:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS \n{cpm:.2f} CPM\n{wps:.2f} WPS\n {wpm:.2f} WPM")

    def reset(self):
        self.runing = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)


TypeSpeed()
