import socket
import threading
import sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


def receive_messages(sock: socket.socket):
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("[INFO] Disconnected from server.")
                break
            print(data.decode("utf-8"), end="")
    except Exception:
        print("[INFO] Connection closed.")
    finally:
        sock.close()
        sys.exit(0)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_HOST, SERVER_PORT))
    except Exception as e:
        print(f"[ERROR] Could not connect: {e}")
        return

    print("Connected to chat server.")
    print("Commands: /nick NAME, /who, /time, /quit")
    print("Type messages and press Enter to send.\n")

    # Start listener thread
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    try:
        while True:
            msg = input()
            if not msg:
                continue
            sock.sendall((msg + "\n").encode("utf-8"))

            if msg.strip().lower() == "/quit":
                break
    except KeyboardInterrupt:
        sock.sendall(b"/quit\n")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
