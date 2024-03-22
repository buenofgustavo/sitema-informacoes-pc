import socket

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        pass
    return False