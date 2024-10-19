import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk

# Function to start file transfer
def send_files():
    # Select multiple files from the system
    file_paths = filedialog.askopenfilenames()
    if not file_paths:
        messagebox.showerror("Error", "No files selected!")
        return

    # Get server address and port from user
    host = simpledialog.askstring("Server IP", "Enter server IP address:", initialvalue='127.0.0.1')
    port = simpledialog.askinteger("Port", "Enter port number:", initialvalue=5001)

    # Establish connection with server
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Send number of files
        client_socket.send(str(len(file_paths)).encode('utf-8'))

        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)

            # Send file metadata (filename and file size)
            client_socket.send(f"{file_name},{file_size}".encode('utf-8'))

            # Create a progress bar
            progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
            progress.pack(pady=20)

            # Send the file data
            bytes_sent = 0
            with open(file_path, "rb") as file:
                while (data := file.read(1024)):
                    client_socket.sendall(data)
                    bytes_sent += len(data)
                    # Update progress
                    progress['value'] = (bytes_sent / file_size) * 100
                    window.update_idletasks()  # Update the GUI

            messagebox.showinfo("Success", f"File '{file_name}' sent successfully!")
            progress.destroy()  # Remove progress bar after each file transfer

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send files: {e}")
    finally:
        client_socket.close()

# GUI Setup
def create_gui():
    global window
    window = tk.Tk()
    window.title("File Transfer Client")
    window.geometry("500x300")
    window.configure(bg="#ADD8E6")  # Background color (light blue)

    # Header label with custom font and color
    header_label = tk.Label(
        window, 
        text="Send Files to Server", 
        font=("Helvetica", 18, "bold"), 
        fg="#388E3C",  # Dark green text
        bg="#ADD8E6",  # Match window background
        padx=10,
        pady=10
    )
    header_label.pack(pady=10)

    # Instruction label
    instruction_label = tk.Label(
        window, 
        text="Select files to send to the server:", 
        font=("Arial", 12), 
        fg="#757575",  # Grey text
        bg="#ADD8E6"  # Match window background
    )
    instruction_label.pack(pady=10)

    # Button for sending files
    send_button = tk.Button(
        window, 
        text="Select Files & Send", 
        command=send_files, 
        font=("Arial", 14, "bold"), 
        bg="#000000",  # Black background
        fg="#FFFFFF",  # White text
        activebackground="#333333",  # Darker grey when clicked
        relief="raised",  # 3D raised effect
        bd=5,  # Border thickness
        padx=20,
        pady=10
    )
    send_button.pack(pady=20)

    # Footer label
    footer_label = tk.Label(
        window, 
        text="Made with ❤️ in Python", 
        font=("Arial", 10, "italic"), 
        fg="#9E9E9E",  # Light grey text
        bg="#ADD8E6"  # Match window background
    )
    footer_label.pack(side="bottom", pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
