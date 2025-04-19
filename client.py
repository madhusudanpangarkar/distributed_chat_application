import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Connection closed.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    name = input("Enter your name: ")
    client.send(f"{name} joined the chat!".encode("utf-8"))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input("")
        client.send(f"{name}: {msg}".encode("utf-8"))

if __name__ == "__main__":
    main()
