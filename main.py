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

# Specify the source directory where the downloads are located
downloads_directory = ""

# Specify the destination directories for different file types
image_directory = ""
video_directory = ""
sound_directory = ""
other_directory = ""

def allocate_downloads():
    # Check if downloads_directory is a valid directory
    if not os.path.isdir(downloads_directory):
        finish_label.configure("Invalid downloads directory.")
        return
    
    # Get the total number of files to allocate
    total_files = len(os.listdir(downloads_directory))

    # Initialize the progress variables
    completed_files = 0
    progress = 0

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

            # Update the progress variables
            completed_files += 1
            progress = completed_files / total_files * 100

            # Update the progress bar
            progress_Bar.set(progress)
            progress_percentage.configure(text=f"{progress:.1f}%")

            # Set the progress to 100% after all files are allocated
            progress_Bar.set(100)
            progress_percentage.configure(text="100%")
            finish_label.configure(text="Completed!")
    else:
        finish_label.configure(text="No files to allocate.")

def select_directory(directory_var):
    directory = filedialog.askdirectory()
    directory_var.set(directory)

def start_allocation():
    try:
        global downloads_directory, image_directory, video_directory, sound_directory, other_directory

        downloads_directory = downloads_var.get()
        image_directory = image_var.get()
        video_directory = video_var.get()
        sound_directory = sound_var.get()
        other_directory = other_var.get()

        if not downloads_directory or not image_directory or not video_directory or not sound_directory or not other_directory:
            raise ValueError("Please select all directories.")
        
        # Check if the selected directories are valid
        if not os.path.isdir(downloads_directory) or not os.path.isdir(image_directory) or not os.path.isdir(video_directory) or not os.path.isdir(sound_directory) or not os.path.isdir(other_directory):
            raise ValueError("Invalid directory selected.")

        allocation_thread = threading.Thread(target=allocate_downloads)
        allocation_thread.start()

        # Clear the progress to 0%
        reset_progress()
        
    except ValueError as e:
        finish_label.configure(text=str(e))
    except:
        finish_label.configure(text="Unable to allocate Files.")
    
def reset_progress():
    progress_Bar.set(0)
    progress_percentage.configure(text="0%")

# Create the main Tkinter window
window = customtkinter.CTk()

# Create StringVars to hold the directory paths
downloads_var = tk.StringVar()
image_var = tk.StringVar()
video_var = tk.StringVar()
sound_var = tk.StringVar()
other_var = tk.StringVar()


# Create UI components
image_1 = ImageTk.PhotoImage(Image.open("./Pattern.png"))
pattern=customtkinter.CTkLabel(master=app, image=image_1)
pattern.pack()

frame_1 = customtkinter.CTkFrame(master=pattern, corner_radius=15)
frame_1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Manage Download Files", justify=customtkinter.CENTER, font=('Bahnschrift SemiBold', 16))
label_1.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

downloads_label = customtkinter.CTkLabel(master=frame_1, text="Download Directory:", width=10, font=('Century Gothic', 12))
downloads_entry = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Download Directory", textvariable=downloads_var)
downloads_button = customtkinter.CTkButton(master=frame_1, text="Select", font=('Bahnschrift SemiBold', 12), width=20, command=lambda: select_directory(downloads_var))

image_label = customtkinter.CTkLabel(master=frame_1, text="Image Directory:", font=('Century Gothic', 12))
image_entry = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Image Directory", textvariable=image_var)
image_button = customtkinter.CTkButton(master=frame_1, text="Select", font=('Bahnschrift SemiBold', 12), width=20, command=lambda: select_directory(image_var))

video_label = customtkinter.CTkLabel(master=frame_1, text="Video Directory:", font=('Century Gothic', 12))
video_entry = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Video Directory", textvariable=video_var)
video_button = customtkinter.CTkButton(master=frame_1, text="Select", font=('Bahnschrift SemiBold', 12), width=20, command=lambda: select_directory(video_var))

sound_label = customtkinter.CTkLabel(master=frame_1, text="Sound Directory:", font=('Century Gothic', 12))
sound_entry = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Sound Directory", textvariable=sound_var)
sound_button = customtkinter.CTkButton(master=frame_1, text="Select", font=('Bahnschrift SemiBold', 12), width=20, command=lambda: select_directory(sound_var))

other_label = customtkinter.CTkLabel(master=frame_1, text="Other Directory:", font=('Century Gothic', 12))
other_entry = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Other Directory", textvariable=other_var)
other_button = customtkinter.CTkButton(master=frame_1, text="Select", font=('Bahnschrift SemiBold', 12), width=20, command=lambda: select_directory(other_var))

button_allocate = customtkinter.CTkButton(master=frame_1, command=start_allocation, text="Start Allocation", font=('Bahnschrift SemiBold', 12),)

finish_label = customtkinter.CTkLabel(master=frame_1, text=" ", font=('Century Gothic', 15))

progress_percentage = customtkinter.CTkLabel(master=frame_1, text="0%")

progress_Bar = customtkinter.CTkProgressBar(master=frame_1, width=200)
progress_Bar.set(0)

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

finish_label.grid(row=8, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

progress_percentage.grid(row=9, column=0, padx=5, pady=5, sticky="nsew", columnspan=3)

progress_Bar.grid(row=10, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)


text_message.grid(row=11, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)


app.mainloop()
