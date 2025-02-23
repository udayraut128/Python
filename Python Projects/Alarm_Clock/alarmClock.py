# Import Required Libraries
from tkinter import *
import datetime
import time
import os
from threading import *

# Create Object
root = Tk()
root.geometry("400x200")

# Function to Play Sound
def play_alarm_sound():
    os.system("mpg123 sound.mp3")  # Change 'sound.mp3' to your actual file

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up!")
            play_alarm_sound()
            break  # Stop looping after alarm rings

# Add Labels, Frame, Button, OptionMenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hour.set("00")
OptionMenu(frame, hour, *[f"{i:02}" for i in range(24)]).pack(side=LEFT)

minute = StringVar(root)
minute.set("00")
OptionMenu(frame, minute, *[f"{i:02}" for i in range(60)]).pack(side=LEFT)

second = StringVar(root)
second.set("00")
OptionMenu(frame, second, *[f"{i:02}" for i in range(60)]).pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
