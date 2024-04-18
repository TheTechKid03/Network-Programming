def Socket():
    import socket

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(15)

    # Get the current send/receive buffer size
    original_send_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    original_receive_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

    print(f"Original Send Buffer Size: {original_send_buffer_size} bytes")
    print(f"Original Receive Buffer Size: {original_receive_buffer_size} bytes")

    # Set a new send buffer size (e.g., 8192 bytes)
    new_send_buffer_size = 4096
    new_receive_buffer_size = 8192

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, new_send_buffer_size)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, new_receive_buffer_size)

    # Get and print the modified send buffer size
    modified_send_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    modified_receive_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

    print(f"Modified Send Buffer Size: {modified_send_buffer_size} bytes")
    print(f"Modified Recieve Buffer Size: {modified_receive_buffer_size} bytes")


Socket()
