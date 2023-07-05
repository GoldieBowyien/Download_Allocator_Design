import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_widget_scaling(1.15)  # widget dimensions and text size
customtkinter.set_window_scaling(1.2)  # window geometry dimensions

app = customtkinter.CTk()
app.geometry("500x580")
app.title("Download Allocator")


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

#Font configuration


# Create UI components
img_1 = ImageTk.PhotoImage(Image.open("Pattern.png"))
pattern=customtkinter.CTkLabel(master=app, image=img_1)
pattern.pack()

frame_1 = customtkinter.CTkFrame(master=pattern, corner_radius=15)
frame_1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Manage Download Files", justify=customtkinter.CENTER, font=('Arial Rounded MT Bold', 15))
label_1.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

downloads_label = customtkinter.CTkLabel(master=frame_1, text="Download Directory:", width=10)
downloads_entry = customtkinter.CTkEntry(master=frame_1, width=158, placeholder_text="Download Directory")
downloads_button = customtkinter.CTkButton(master=frame_1, text="Select", width=20, command=lambda: select_directory(download_var))

image_label = customtkinter.CTkLabel(master=frame_1, text="Image Directory:")
image_entry = customtkinter.CTkEntry(master=frame_1, width=158, placeholder_text="Image Directory")
image_button = customtkinter.CTkButton(master=frame_1, text="Select", width=20, command=lambda: select_directory(image_var))

video_label = customtkinter.CTkLabel(master=frame_1, text="Video Directory:")
video_entry = customtkinter.CTkEntry(master=frame_1, width=158, placeholder_text="Video Directory")
video_button = customtkinter.CTkButton(master=frame_1, text="Select", width=20, command=lambda: select_directory(video_var))

sound_label = customtkinter.CTkLabel(master=frame_1, text="Sound Directory:")
sound_entry = customtkinter.CTkEntry(master=frame_1, width=158, placeholder_text="Sound Directory")
sound_button = customtkinter.CTkButton(master=frame_1, text="Select", width=20, command=lambda: select_directory(sound_var))

other_label = customtkinter.CTkLabel(master=frame_1, text="Other Directory:")
other_entry = customtkinter.CTkEntry(master=frame_1, width=158, placeholder_text="Other Directory")
other_button = customtkinter.CTkButton(master=frame_1, text="Select", width=20, command=lambda: select_directory(other_var))

button_allocate = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Start Allocation")

entry_allocate = customtkinter.CTkEntry(master=frame_1, placeholder_text="Start Allocation")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Remember me")

text_message = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_message.insert("2.0", "\n\n")

# Grid layout for UI components
downloads_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
downloads_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
downloads_button.grid(row=2, column=2, padx=10, pady=10, sticky="e")

image_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
image_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
image_button.grid(row=3, column=2, padx=10, pady=10, sticky="e")

video_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
video_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
video_button.grid(row=4, column=2, padx=10, pady=10, sticky="e")

sound_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
sound_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")
sound_button.grid(row=5, column=2, padx=10, pady=10, sticky="e")

other_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
other_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w", columnspan=2)
other_button.grid(row=6, column=2, padx=10, pady=10, sticky="e")

button_allocate.grid(row=7, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

entry_allocate.grid(row=8, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

checkbox_1.grid(row=9, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

text_message.grid(row=10, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)


app.mainloop()
