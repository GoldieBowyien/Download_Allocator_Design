import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry(f"{1100}x{580}")
app.title("Download Allocator")
app.config(bg="#3498DB")


def button_callback():
    print("Button click")

# Specify the source directory where the downloads are located
downloads_directory = ""

# Specify the destination directories for different file types
image_directory = ""
video_directory = ""
sound_directory = ""
other_directory = ""

def allocate_downloads():
    # Iterate over each file in the downloads directory
    for filename in os.listdir(downloads_directory):
        # Get the full path of the file
        file_path = os.path.join(downloads_directory, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Allocate the file to the corresponding folder based on its extension
            if file_extension in ('.jpg', '.jpeg', '.png', '.gif'):
                destination_folder = image_directory
            elif file_extension in ('.mp4', '.avi', '.mkv'):
                destination_folder = video_directory
            elif file_extension in ('.mp3', '.wav', ".flac"):
                destination_folder = sound_directory
            else:
                destination_folder = other_directory
            
            # Create the destination directory if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)
            
            # Move the file to the destination directory
            shutil.move(file_path, os.path.join(destination_folder, filename))

def select_directory(directory_var):
    directory = filedialog.askdirectory()
    directory_var.set(directory)

def start_allocation():
    global downloads_directory, image_directory, video_directory, sound_directory, other_directory

    downloads_directory = downloads_var.get()
    image_directory = image_var.get()
    video_directory = video_var.get()
    sound_directory = sound_var.get()
    other_directory = other_var.get()

    allocation_thread = threading.Thread(target=allocate_downloads)
    allocation_thread.start()







frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(pady=20, padx=60)

label_1 = customtkinter.CTkLabel(master=frame_1,text="Manage Download Files", justify=customtkinter.LEFT)
label_1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

downloads_label = customtkinter.CTkLabel(master=frame_1, text="Download Directory:", width=10)
downloads_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

downloads_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Download Directory")
downloads_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

#downloads_button = customtkinter.CTkButton(master=frame_1, text="Select", command=lambda: select_directory(download_var))
#downloads_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

image_label = customtkinter.CTkLabel(master=frame_1, text="Image Directory:")
image_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

image_entry = customtkinter.CTkEntry(master=frame_1)
image_entry.grid(row=0, column=0, padx=10, pady=10, sticky="e")

#image_button = customtkinter.CTkButton(master=frame_1, text="Select", command=lambda: select_directory(image_var))
#image_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

video_label = customtkinter.CTkLabel(master=frame_1, text="Video Directory:")
video_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

video_entry = customtkinter.CTkEntry(master=frame_1)
video_entry.grid(row=0, column=0, padx=10, pady=10, sticky="e")

#video_button = customtkinter.CTkButton(master=frame_1, text="Select", command=lambda: select_directory(video_var))
#video_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

sound_label = customtkinter.CTkLabel(master=frame_1, text="Sound Directory:")
sound_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

sound_entry = customtkinter.CTkEntry(master=frame_1)
sound_entry.grid(row=0, column=0, padx=10, pady=10, sticky="e")

#sound_button = customtkinter.CTkButton(master=frame_1, text="Select", command=lambda: select_directory(sound_var))
#sound_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

other_label = customtkinter.CTkLabel(master=frame_1, text="Other Directory:")
other_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

other_entry = customtkinter.CTkEntry(master=frame_1)
other_entry.grid(row=0, column=0, padx=10, pady=10, sticky="e")

#other_button = customtkinter.CTkButton(master=frame_1, text="Select", command=lambda: select_directory(other_var))
#other_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")


button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Start Allocation")
button_1.grid(row=0, column=0, padx=10, pady=10, sticky="e")


entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Start Allocation")
entry_1.grid(row=0, column=0, padx=10, pady=10, sticky="e")



checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Remember me")
checkbox_1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
text_1.insert("2.0", "Message here\n\n")

app.mainloop()
