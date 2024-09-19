import socket

# Define the UDP IP address and port to listen on
UDP_IP = "127.0.0.1"
UDP_PORT = 20777

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")

while True:
    data = sock.recv(4096)

    packet_id = data[6]

    match packet_id:
        case 1:
            with open('data/session.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 2:
            with open('data/lapdata.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 3:
            with open('data/event.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 4:
            with open('data/participants.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 8:
            with open('data/classification.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 9:
            with open('data/lobbyinfo.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 10:
            with open('data/cardamage.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
        case 12:
            with open('data/tyresets.txt', 'a') as f:
                f.write(str(data)[2:-1] + '<mtc>')
