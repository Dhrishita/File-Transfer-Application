# File-Transfer-Application
A Python-based file transfer application that allows users to send multiple files from a client to a server using socket programming. The application features a graphical user interface (GUI) for easy file selection and transfer and uses a simple server to receive and store the files on the server side.

## Table of Contents
- [Problem Statement](#problem-statement)
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologie-sused)
- [Installation](#installation)
- [Usage](#usage)
- [Working of the Application (Socket Programming)](#working-of-the-application-socketprogramming)
- [Error Handling](#error-handling)
- [Contact](#contact)

## Problem Statement

In today's digital age, transferring files between devices quickly and efficiently is essential for both personal and professional use. Many existing file transfer methods are either complicated, require specific software, or lack user-friendly interfaces.

## Introduction

In an era where data sharing has become an integral part of both personal and professional communication, efficient and reliable file transfer solutions are essential. Traditional methods of file transfer, such as email attachments or external storage devices, often come with limitations in terms of file size, speed, and security. As a result, there is a growing demand for customizable, user-friendly applications that facilitate seamless file sharing between devices.

This project presents a File Transfer Application developed using Python, leveraging the capabilities of socket programming and a graphical user interface (GUI) provided by Tkinter. The application aims to simplify the process of sending multiple files from a client to a server, providing users with a straightforward interface to select files, monitor transfer progress, and receive feedback throughout the process.


## Features

- **User Friendly GUI** - The application features an intuitive interface that guides users through the file selection and transfer process, making it accessible to individuals with varying levels of technical expertise.
- **Multiple File Transfer** - Users can select and send multiple files simultaneously, enhancing efficiency and convenience.
- **Real Time Progress Monitoring** - A progress bar visually represents the status of each file transfer, allowing users to track progress and estimate remaining time.
- **Robust Communication Protocol** - Utilizing socket programming, the application establishes reliable communication between the client and server, ensuring that files are transferred accurately and securely.
- **Error Handling** - The application is designed to handle various errors gracefully, providing users with informative messages in case of issues such as connection failures or file transfer interruptions.
  
## Technologies Used

- **Language** - Python
- **GUI Framework** - Tkinter
- **Network Communication** - Sockets (TCP)
- **File Transfer** - Custom protocol over socket communication

  
## Installation

1. Clone this repository to your Raspberry Pi:
   
   ```bash
   git clone https://github.com/yourusername/file-transfer-application.git
   cd file-transfer-application


2. Install the required packages using pip:

   ```bash
   pip install tkinter


3. Make sure to run the server first, followed by the client.

## Usage

- Running the Server
  
  - Open a terminal window and navigate to the project folder.
  - Start the server:

     ```bash
     python3 server.py

- Running the Client

  - Open a terminal window on another laptop and navigate to the project folder.
  - Run the client to open the GUI:

     ```bash
     python client.py
 
  - Select the files you want to send using the GUI interface.
  - Enter the server's IP address and port number (default: 127.0.0.1 and 5001).
  - The progress of the file transfer will be displayed, and a confirmation message will appear once the file is successfully sent.
  

## Working of the Application (Socket Programming)

The server listens for incoming connections, receives file metadata (name and size), and then saves the file data to the current working directory. Files are prefixed with received_ to distinguish them from original files.

Example Workflow

- **Start the server** - The server begins listening on 0.0.0.0:5001 for incoming connections.
- **Send files via client** - The user selects files, enters the server details, and starts the file transfer process.
- **Receive files on the server** - The server receives each file one by one, storing them locally with the received_ prefix.

## Error Handling

- **No files selected** - The client displays an error message if no files are chosen.
- **Connection issues** - The client and server handle connection failures gracefully.
- **File transfer errors** - If a file fails to transfer, the application shows an error message.


## Contact
If you have any questions or suggestions, feel free to open an issue or contact:
Dhrishita Parve: dhrishitap18@gmail.com
