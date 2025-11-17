import socket
import threading
import datetime

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 5000        # you can change this if needed

clients = {}       # socket -> nickname


def broadcast(message, sender_sock=None):
    """Send message to all connected clients except optional sender."""
    for sock in list(clients.keys()):
        if sock is sender_sock:
            continue
        try:
            sock.sendall(message.encode("utf-8"))
        except Exception:
            # If send fails, drop that client
            remove_client(sock)


def remove_client(sock):
    """Remove client from dict and close socket."""
    nickname = clients.get(sock, "Unknown")
    if sock in clients:
        del clients[sock]
    try:
        sock.close()
    except Exception:
        pass
    print(f"[INFO] {nickname} disconnected.")
    broadcast(f"[SERVER] {nickname} has left the chat.\n")


def handle_client(sock, address):
    """Handle messages from a single client."""
    print(f"[NEW CONNECTION] {address}")

    # Default nickname based on address
    nickname = f"User_{address[1]}"
    clients[sock] = nickname
    sock.sendall(f"[SERVER] Welcome, {nickname}!\n".encode("utf-8"))
    broadcast(f"[SERVER] {nickname} has joined the chat.\n", sender_sock=sock)

    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break  # client closed connection

            text = data.decode("utf-8").strip()
            if not text:
                continue

            # Handle commands that start with "/"
            if text.startswith("/"):
                parts = text.split(maxsplit=1)
                command = parts[0].lower()

                # /nick NEWNAME
                if command == "/nick":
                    if len(parts) < 2:
                        sock.sendall(b"[SERVER] Usage: /nick NEWNAME\n")
                        continue
                    new_name = parts[1].strip()
                    old_name = clients[sock]
                    clients[sock] = new_name
                    sock.sendall(
                        f"[SERVER] Nickname changed to {new_name}\n".encode("utf-8")
                    )
                    broadcast(
                        f"[SERVER] {old_name} is now known as {new_name}\n",
                        sender_sock=sock,
                    )

                # /who  → list users
                elif command == "/who":
                    names = ", ".join(clients.values())
                    sock.sendall(
                        f"[SERVER] Connected users: {names}\n".encode("utf-8")
                    )

                # /time → server time (extra nice-to-have)
                elif command == "/time":
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    sock.sendall(
                        f"[SERVER] Server time: {now}\n".encode("utf-8")
                    )

                # /quit → disconnect
                elif command == "/quit":
                    sock.sendall(b"[SERVER] Goodbye!\n")
                    break

                else:
                    sock.sendall(b"[SERVER] Unknown command.\n")

            else:
                # Normal chat message → broadcast
                nickname = clients.get(sock, "Unknown")
                broadcast(f"{nickname}: {text}\n", sender_sock=sock)

    except Exception as e:
        print(f"[ERROR] {address}: {e}")

    finally:
        remove_client(sock)


def main():
    print(f"[STARTING] Chat server starting on {HOST}:{PORT}")
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))
    server_sock.listen()

    try:
        while True:
            client_sock, addr = server_sock.accept()
            thread = threading.Thread(
                target=handle_client, args=(client_sock, addr), daemon=True
            )
            thread.start()
    finally:
        server_sock.close()


if __name__ == "__main__":
    main()
