import socket
import numpy as np
import cv2
import struct
import time
import argparse

# Server IP address and port
parser = argparse.ArgumentParser(description="MPU deploy host viewer")
parser.add_argument("Board_IP",help= "Please input your board IP e.g 192.168.1.11")
args= parser.parse_args()


SERVER_IP = args.Board_IP # Change this if your server is on a different machine
PORT = 8080
 
def receive_frame(sock):
    # First, receive the size of the frame
    print("frame process")
    data = sock.recv(4)
    print("Data:",data)
    if not data:
        print("data is None")
        return None
 
    # Convert the size from network byte order to host byte order
    frame_size = struct.unpack('!I', data)[0]
    print(f"Receiving frame of size: {frame_size}")
 
    # Now receive the actual frame data
    frame_data = b''
    frame_d = b''
    while  len(frame_data) < frame_size:
        print(frame_size)
        packet = sock.recv(frame_size - len(frame_data))
        if not packet:
            return None
        frame_data += packet
    #frame = np.frombuffer(frame_data, dtype=np.float16)  # Read as fp16
    #frame = (frame * 255).astype(np.uint8)  # Normalize and convert to uint8
    frame = np.frombuffer(frame_data, dtype=np.uint8)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    return frame
 
def main():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    try:
        # Connect to the server
        sock.connect((SERVER_IP, PORT))
        print("Connected to the server.")
 
        while True:
            print("flag 1")
            frame = receive_frame(sock)
            print(frame)
            if frame is None:
                print("Failed to receive frame or connection closed.")
                break

            # Display the frame
            cv2.imshow('Received Video', frame)
 
            # Press 'ESC' to exit
            if cv2.waitKey(1) == 27:
                break
 
    finally:
        # Clean up
        sock.close()
        cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()
