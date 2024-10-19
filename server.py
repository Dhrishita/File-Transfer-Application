import socket
import os

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5001))  # Listen on all interfaces
    server_socket.listen(5)
    print("[*] Server started on 0.0.0.0:5001")

    while True:
        conn, addr = server_socket.accept()
        print(f"[+] Connection from {addr}")
        
        # Receive the number of files
        num_files = conn.recv(1024).decode('utf-8')
        if not num_files:
            conn.close()
            continue
        num_files = int(num_files)
        print(f"[*] Expecting {num_files} files")

        for _ in range(num_files):
            # Receive file metadata (filename and file size)
            file_info = conn.recv(1024)
            if not file_info:
                break
            
            try:
                file_info = file_info.decode('latin-1')
                file_name, file_size = file_info.split(',')
                file_size = int(file_size)
                print(f"[*] Receiving file: {file_name}, Size: {file_size} bytes")
            except ValueError as e:
                print(f"[!] Error unpacking file info: {e}")
                break
            
            # Prepare to receive the file
            received_file_path = os.path.join(os.getcwd(), f"received_{file_name}")
            with open(received_file_path, "wb") as file:
                bytes_received = 0
                while bytes_received < file_size:
                    bytes_read = conn.recv(4096)
                    if not bytes_read:
                        break
                    file.write(bytes_read)
                    bytes_received += len(bytes_read)

            print(f"[+] File received successfully as '{received_file_path}'")
        
        conn.close()

if __name__ == "__main__":
    start_server()
